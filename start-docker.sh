#!/bin/bash

# 应用 collections 补丁
python collections_patch.py

# 复制 Docker 配置文件
cp config-docker.ini config.ini

# 等待 MySQL 启动
echo "等待 MySQL 启动..."
while ! nc -z db 3306; do
  sleep 1
done
echo "MySQL 已启动"

# 运行 Django 服务器
echo "启动 Django 服务器..."
python manage.py runserver 0.0.0.0:8080 