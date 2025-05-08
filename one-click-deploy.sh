#!/bin/bash

echo "====================================================="
echo "         工艺品交易系统 - CentOS一键部署脚本"
echo "====================================================="

# 检查是否为root用户
if [ "$(id -u)" != "0" ]; then
   echo "此脚本需要root权限运行，请使用sudo或以root用户身份运行"
   exit 1
fi

# 检查并安装Docker
echo "[1/7] 检查并安装Docker..."
if ! command -v docker &> /dev/null; then
    echo "Docker未安装，正在安装..."
    yum install -y yum-utils
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    yum install -y docker-ce docker-ce-cli containerd.io
    systemctl start docker
    systemctl enable docker
    echo "Docker安装完成！"
else
    echo "Docker已安装，跳过安装步骤"
fi

# 检查并安装Docker Compose
echo "[2/7] 检查并安装Docker Compose..."
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose未安装，正在安装..."
    curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose 2>/dev/null || true
    echo "Docker Compose安装完成！"
else
    echo "Docker Compose已安装，跳过安装步骤"
fi

# 确保脚本可执行
chmod +x docker_image_fix.sh

# 3. 创建必要的目录
echo "[3/7] 创建必要的目录..."
mkdir -p media/upload
mkdir -p media/front

# 4. 准备图片资源
echo "[4/7] 准备图片资源..."
cp -r templates/front/*.jpg media/upload/ 2>/dev/null || true
cp -r templates/front/*.jpg media/front/ 2>/dev/null || true

# 创建调试脚本
echo "[4.5/7] 创建调试脚本..."

# 创建媒体URL配置脚本
cat > media_url_config.py << 'EOL'
#!/usr/bin/env python
import os
import sys

print("========== 媒体URL配置脚本开始执行 ==========")
print(f"当前工作目录: {os.getcwd()}")

# 要修改的文件
filepath = "dj2/urls.py"
print(f"准备修改文件: {filepath}")

# 检查文件是否存在
if not os.path.exists(filepath):
    print(f"错误: 文件 {filepath} 不存在!")
    sys.exit(1)
else:
    print(f"文件 {filepath} 存在，准备读取内容")

# 读取文件内容
try:
    with open(filepath, 'r') as file:
        content = file.read()
    print(f"成功读取文件 {filepath}, 长度: {len(content)} 字符")
except Exception as e:
    print(f"读取文件时出错: {str(e)}")
    sys.exit(1)

# 导入需要的模块
print("检查是否需要导入MEDIA_ROOT和MEDIA_URL...")
if "from dj2.settings import MEDIA_ROOT" not in content:
    print("需要添加MEDIA_ROOT和MEDIA_URL导入")
    original_content = content
    content = content.replace(
        "from dj2.settings import dbName as schemaName", 
        "from dj2.settings import dbName as schemaName\nfrom dj2.settings import MEDIA_ROOT, MEDIA_URL"
    )
    if original_content == content:
        print("警告: 无法找到合适的位置添加导入语句")
    else:
        print("成功添加MEDIA_ROOT和MEDIA_URL导入")
else:
    print("MEDIA_ROOT和MEDIA_URL导入已存在，无需添加")

# 添加媒体URL配置
print("检查是否需要添加媒体URL配置...")
if "re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})" not in content:
    print("需要添加媒体URL配置")
    
    if "path(r'null',views.null)," in content:
        print("找到插入点: path(r'null',views.null),")
        original_content = content
        content = content.replace(
            "path(r'null',views.null),", 
            "path(r'null',views.null),\n    # 添加媒体文件的URL配置\n    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),"
        )
        if original_content == content:
            print("警告: 替换操作未成功")
        else:
            print("成功在null路径后添加媒体URL配置")
    else:
        print("找不到null路径，尝试在urlpatterns列表末尾添加")
        original_content = content
        content = content.replace(
            "]", 
            "    # 添加媒体文件的URL配置\n    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),\n]"
        )
        if original_content == content:
            print("警告: 在urlpatterns列表末尾添加失败")
        else:
            print("成功在urlpatterns列表末尾添加媒体URL配置")
else:
    print("媒体URL配置已存在，无需添加")

# 写回文件
print(f"将修改后的内容写回 {filepath}...")
try:
    with open(filepath, 'w') as file:
        file.write(content)
    print(f"成功写入文件 {filepath}")
except Exception as e:
    print(f"写入文件时出错: {str(e)}")
    sys.exit(1)

# 检查是否存在必要的导入和配置  
print("验证修改结果...")
with open(filepath, 'r') as file:
    new_content = file.read()
    
if "from dj2.settings import MEDIA_ROOT" in new_content:
    print("MEDIA_ROOT导入存在 ✓")
else:
    print("错误: MEDIA_ROOT导入不存在 ✗")
    
if "re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})" in new_content:
    print("媒体URL配置存在 ✓")
else:
    print("错误: 媒体URL配置不存在 ✗")

# 检查媒体目录权限
print("\n检查媒体目录权限...")
media_dir = "media"
if os.path.exists(media_dir):
    print(f"媒体目录 {media_dir} 存在")
    try:
        os.chmod(media_dir, 0o755)
        print(f"已设置 {media_dir} 目录权限为 755")
        
        # 检查子目录
        for subdir in ["upload", "front"]:
            subdir_path = os.path.join(media_dir, subdir)
            if os.path.exists(subdir_path):
                print(f"子目录 {subdir_path} 存在")
                os.chmod(subdir_path, 0o755)
                print(f"已设置 {subdir_path} 目录权限为 755")
                
                # 列出子目录中的文件数量
                files = [f for f in os.listdir(subdir_path) if f.endswith('.jpg')]
                print(f"{subdir_path} 目录中有 {len(files)} 个jpg文件")
            else:
                print(f"警告: 子目录 {subdir_path} 不存在")
    except Exception as e:
        print(f"设置权限时出错: {str(e)}")
else:
    print(f"警告: 媒体目录 {media_dir} 不存在")

print("========== 媒体URL配置脚本执行完成 ==========")
EOL

# 创建媒体文件服务调试脚本
cat > debug_media_serving.py << 'EOL'
#!/usr/bin/env python
import os
import sys
from pathlib import Path

print("========== 媒体文件服务调试脚本开始执行 ==========")

# 检查当前工作目录
base_dir = os.getcwd()
print(f"当前工作目录: {base_dir}")

# 检查Django设置文件
settings_path = os.path.join(base_dir, "dj2", "settings.py")
print(f"检查Django设置文件: {settings_path}")

if not os.path.exists(settings_path):
    print(f"错误: Django设置文件不存在: {settings_path}")
    sys.exit(1)

# 解析设置文件中的媒体配置
try:
    with open(settings_path, 'r') as f:
        settings_content = f.read()
        print("成功读取设置文件")
        
        # 提取MEDIA_URL和MEDIA_ROOT
        media_url_line = next((line for line in settings_content.splitlines() if "MEDIA_URL" in line), None)
        media_root_line = next((line for line in settings_content.splitlines() if "MEDIA_ROOT" in line), None)
        
        if media_url_line:
            print(f"MEDIA_URL 设置: {media_url_line.strip()}")
        else:
            print("警告: 未找到MEDIA_URL设置")
            
        if media_root_line:
            print(f"MEDIA_ROOT 设置: {media_root_line.strip()}")
        else:
            print("警告: 未找到MEDIA_ROOT设置")
except Exception as e:
    print(f"读取设置文件时出错: {str(e)}")

# 检查URL配置
urls_path = os.path.join(base_dir, "dj2", "urls.py")
print(f"\n检查URL配置文件: {urls_path}")

if not os.path.exists(urls_path):
    print(f"错误: URL配置文件不存在: {urls_path}")
    sys.exit(1)

try:
    with open(urls_path, 'r') as f:
        urls_content = f.read()
        print("成功读取URL配置文件")
        
        # 检查是否导入了serve和媒体设置
        if "from django.views.static import serve" in urls_content:
            print("static.serve 导入存在 ✓")
        else:
            print("错误: static.serve 导入不存在 ✗")
            
        if "from dj2.settings import MEDIA_ROOT" in urls_content:
            print("MEDIA_ROOT 导入存在 ✓")
        else:
            print("错误: MEDIA_ROOT 导入不存在 ✗")
            
        # 检查媒体URL配置
        if "re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})" in urls_content:
            print("媒体URL配置存在 ✓")
        else:
            print("错误: 媒体URL配置不存在 ✗")
except Exception as e:
    print(f"读取URL配置文件时出错: {str(e)}")

# 检查媒体目录和文件
media_dir = os.path.join(base_dir, "media")
print(f"\n检查媒体目录: {media_dir}")

if os.path.exists(media_dir):
    print(f"媒体目录存在 ✓")
    
    # 检查权限
    stat_info = os.stat(media_dir)
    print(f"媒体目录权限: {oct(stat_info.st_mode)[-3:]}")
    
    # 检查子目录
    for subdir in ["upload", "front"]:
        subdir_path = os.path.join(media_dir, subdir)
        if os.path.exists(subdir_path):
            print(f"子目录 {subdir} 存在 ✓")
            
            # 检查权限
            subdir_stat = os.stat(subdir_path)
            print(f"子目录 {subdir} 权限: {oct(subdir_stat.st_mode)[-3:]}")
            
            # 列出子目录中的文件
            files = [f for f in os.listdir(subdir_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            print(f"子目录 {subdir} 中有 {len(files)} 个图片文件")
            
            if files:
                print(f"示例文件: {', '.join(files[:3])}")
                
                # 选择第一个文件检查
                sample_file = os.path.join(subdir_path, files[0])
                sample_stat = os.stat(sample_file)
                print(f"示例文件 {files[0]} 权限: {oct(sample_stat.st_mode)[-3:]}")
                print(f"示例文件 {files[0]} 大小: {sample_stat.st_size} 字节")
        else:
            print(f"错误: 子目录 {subdir} 不存在 ✗")
else:
    print(f"错误: 媒体目录不存在 ✗")

# 检查容器环境
if os.path.exists("/.dockerenv"):
    print("\n检测到Docker容器环境")
    
    # 检查启动脚本
    start_script = os.path.join(base_dir, "start.sh")
    if os.path.exists(start_script):
        print(f"启动脚本存在: {start_script} ✓")
        
        try:
            with open(start_script, 'r') as f:
                start_content = f.read()
                print(f"启动脚本内容长度: {len(start_content)} 字符")
                
                # 检查关键设置
                if "chmod -R 755 /app/media" in start_content:
                    print("启动脚本包含媒体目录权限设置 ✓")
                else:
                    print("警告: 启动脚本未包含媒体目录权限设置")
        except Exception as e:
            print(f"读取启动脚本时出错: {str(e)}")
    else:
        print(f"警告: 启动脚本不存在: {start_script}")
else:
    print("\n当前不在Docker容器环境中")

print("\n总结:")
print("1. 创建一个测试媒体文件访问URL")
print("   - 根据典型图片路径，访问URL应该是: /media/front/背景.jpg")
print("2. 检查浏览器网络请求，确认是否有404错误")
print("3. 监控Django日志，查看媒体文件请求处理情况")

print("\n建议:")
print("1. 确保urls.py中正确配置了媒体文件URL路径")
print("2. 确保媒体文件目录权限为755")
print("3. 重启Django服务器，刷新浏览器缓存")
print("4. 检查Django DEBUG设置是否启用")

print("========== 媒体文件服务调试脚本执行完成 ==========")
EOL

chmod +x media_url_config.py
chmod +x debug_media_serving.py

# 5. 创建Docker配置文件
echo "[5/7] 创建Docker配置文件..."
cat > docker-compose.yml << 'EOL'
version: '3'

services:
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: django06g8e
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-proot_password"]
      interval: 5s
      timeout: 5s
      retries: 10

  web:
    build:
      context: .
      dockerfile: Dockerfile.simple
    restart: always
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "8080:8080"
    volumes:
      - ./media:/app/media
      - ./templates:/app/templates
    environment:
      - MYSQL_HOST=db
      - MYSQL_PORT=3306
      - MYSQL_USER=root
      - MYSQL_PASSWORD=root_password
      - MYSQL_DATABASE=django06g8e
      - DEBUG=1

volumes:
  mysql_data:
EOL

# 6. 创建简化版的Dockerfile
echo "[6/7] 创建Dockerfile..."
cat > Dockerfile.simple << 'EOL'
FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    netcat-traditional \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .
COPY collections_patch.py .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysqlclient

# 复制应用代码
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV DEBUG=1

# 应用collections补丁
RUN python collections_patch.py

# 创建启动脚本
RUN echo '#!/bin/bash\n\
\n\
echo "===== 容器启动脚本开始执行 ====="\n\
\n\
echo "当前工作目录: $(pwd)"\n\
echo "文件列表:"\n\
ls -la\n\
\n\
echo "等待MySQL启动..."\n\
until nc -z -v -w30 db 3306; do\n\
  echo "等待MySQL连接..."\n\
  sleep 2\n\
done\n\
echo "MySQL已启动，开始运行应用..."\n\
\n\
echo "复制Docker配置文件..."\n\
cp /app/config-docker.ini /app/config.ini\n\
\n\
echo "运行图片修复脚本..."\n\
bash /app/docker_image_fix.sh\n\
\n\
echo "设置媒体文件URL..."\n\
python /app/media_url_config.py\n\
\n\
echo "运行媒体文件调试脚本..."\n\
python /app/debug_media_serving.py\n\
\n\
echo "设置媒体目录权限..."\n\
chmod -R 755 /app/media\n\
\n\
echo "检查media目录内容:"\n\
ls -la /app/media\n\
echo "检查media/front目录内容:"\n\
ls -la /app/media/front\n\
echo "检查media/upload目录内容:"\n\
ls -la /app/media/upload\n\
\n\
echo "启动Django应用..."\n\
python manage.py runserver 0.0.0.0:8080\n\
' > /app/start.sh

RUN chmod +x /app/start.sh

# 创建专用配置文件
RUN echo '[sql]\n\
type = mysql\n\
host = db\n\
port = 3306\n\
user = root\n\
passwd = root_password\n\
db = django06g8e\n\
charset = utf8\n\
hasHadoop=否\n\
[redis]\n\
host = 127.0.0.1\n\
port = 6379\n\
passwd = 123456\n\
' > /app/config-docker.ini

# 暴露端口
EXPOSE 8080

# 启动命令
CMD ["/app/start.sh"]
EOL

# 7. 构建并启动容器
echo "[7/7] 构建并启动Docker容器..."
docker-compose up -d --build

# 等待服务启动
echo "等待服务完全启动..."
sleep 15

# 获取服务器IP地址
SERVER_IP=$(hostname -I | awk '{print $1}')

# 打印访问信息
echo ""
echo "====================================================="
echo "              部署完成！"
echo "====================================================="
echo "前台访问地址: http://${SERVER_IP}:8080/front/index.html"
echo "后台访问地址: http://${SERVER_IP}:8080/admin/dist/index.html"
echo ""
echo "默认管理员账号: admin"
echo "默认管理员密码: admin"
echo "====================================================="
echo ""
echo "查看容器状态: docker-compose ps"
echo "查看应用日志: docker-compose logs -f web"
echo "停止服务: docker-compose down"
echo "====================================================="
echo ""
echo "调试命令："
echo "1. 进入容器: docker exec -it django06g8e_web_1 /bin/bash"
echo "2. 在容器内运行调试脚本: python /app/debug_media_serving.py"
echo "3. 检查日志: docker-compose logs -f web | grep -i media"
echo "4. 重启容器: docker-compose restart web"
echo "=====================================================" 