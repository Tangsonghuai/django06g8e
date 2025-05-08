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

# 创建并准备媒体目录
RUN mkdir -p /app/media/upload /app/media/front
# 复制模板中的图片到媒体目录并修复基础URL
RUN chmod +x /app/docker_image_fix.sh /app/docker_baseurl_fix.sh

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# 应用collections补丁
RUN python collections_patch.py

# 暴露端口
EXPOSE 8080

# 启动命令（先运行图片修复脚本和URL修复脚本，然后启动应用）
CMD ["sh", "-c", "/app/docker_image_fix.sh && /app/docker_baseurl_fix.sh && python manage.py runserver 0.0.0.0:8080"] 