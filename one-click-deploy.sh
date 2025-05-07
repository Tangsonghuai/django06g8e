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

# 应用collections补丁
RUN python collections_patch.py

# 等待数据库启动脚本
RUN echo '#!/bin/bash\n\
echo "等待MySQL启动..."\n\
until nc -z -v -w30 db 3306; do\n\
  echo "等待MySQL连接..."\n\
  sleep 2\n\
done\n\
echo "MySQL已启动，开始运行应用..."\n\
\n\
# 复制Docker配置文件\n\
cp /app/config-docker.ini /app/config.ini\n\
\n\
# 运行图片修复脚本\n\
bash /app/docker_image_fix.sh\n\
\n\
# 启动Django应用\n\
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