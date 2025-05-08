#!/bin/bash

# 工艺品交易系统 - 自定义域名部署脚本

# 输出带颜色的信息
function print_info() {
    echo -e "\033[1;34m[信息]\033[0m $1"
}

function print_success() {
    echo -e "\033[1;32m[成功]\033[0m $1"
}

function print_error() {
    echo -e "\033[1;31m[错误]\033[0m $1"
}

function print_usage() {
    echo "用法: $0 [域名或IP地址]"
    echo "例子: $0 192.168.1.10    # 使用服务器IP"
    echo "      $0 example.com     # 使用域名"
    echo "      $0                 # 自动检测服务器IP"
}

# 如果提供了参数，使用它作为域名
if [ -n "$1" ]; then
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
        print_usage
        exit 0
    fi
    DOMAIN=$1
    print_info "使用提供的域名或IP: $DOMAIN"
else
    # 尝试获取服务器IP
    SERVER_IP=$(hostname -I | awk '{print $1}')
    if [ -n "$SERVER_IP" ]; then
        DOMAIN=$SERVER_IP
        print_info "自动检测到服务器IP: $DOMAIN"
    else
        DOMAIN="localhost"
        print_info "无法检测服务器IP，使用默认值: $DOMAIN"
    fi
fi

# 导出环境变量
export SITE_DOMAIN=$DOMAIN

print_info "正在部署工艺品交易系统，使用域名: $DOMAIN"

# 构建并启动容器
docker-compose down
docker-compose up -d --build

# 等待服务启动
print_info "等待服务启动..."
sleep 10

print_success "工艺品交易系统已部署！"
echo ""
echo "前台访问地址: http://$DOMAIN:8080/front/index.html"
echo "后台访问地址: http://$DOMAIN:8080/admin/dist/index.html"
echo ""
echo "默认管理员账号: admin"
echo "默认管理员密码: admin" 