#!/bin/bash

echo "开始构建工艺品交易系统Docker镜像..."

# 确保脚本可执行
chmod +x entrypoint.sh
chmod +x start-docker.sh

# 构建开发环境镜像
echo "构建开发环境镜像..."
docker-compose build

# 构建生产环境镜像
echo "构建生产环境镜像..."
docker-compose -f docker-compose-prod.yml build

echo "Docker镜像构建完成!"
echo "可以使用以下命令启动开发环境:"
echo "docker-compose up -d"
echo "或者使用以下命令启动生产环境:"
echo "docker-compose -f docker-compose-prod.yml up -d" 