#!/bin/sh

# 安装netcat用于检查端口
apt-get update && apt-get install -y netcat-openbsd

# 确保脚本可执行
chmod +x /app/start-docker.sh
chmod +x /app/docker_image_fix.sh

# 应用collections补丁
python /app/collections_patch.py

# 运行图片修复脚本
python /app/docker_image_fix.sh

# 复制Docker配置文件
cp /app/config-docker.ini /app/config.ini

# 等待MySQL可用
echo "等待 MySQL 启动..."
while ! nc -z db 3306; do
  echo "等待MySQL连接..."
  sleep 2
done
echo "MySQL 已启动"

# 运行Django服务器
exec "$@" 