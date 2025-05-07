#!/bin/bash

echo "开始启动工艺品交易系统..."

# 确保脚本可执行
chmod +x docker_image_fix.sh

# 构建并启动Docker容器
echo "正在构建和启动容器..."
docker-compose -f docker-compose-simple.yml up -d

echo "等待服务启动..."
sleep 5

echo "服务已成功启动！"
echo "访问地址: http://localhost:8080/front/index.html"
echo "后台地址: http://localhost:8080/admin/dist/index.html"
echo ""
echo "管理员账号: admin"
echo "管理员密码: admin" 