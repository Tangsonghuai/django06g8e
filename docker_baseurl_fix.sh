#!/bin/bash

# 图片URL修复脚本：解决Docker容器中图片无法显示的问题
# 适用于所有Django06g8e部署环境

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

function print_warning() {
    echo -e "\033[1;33m[警告]\033[0m $1"
}

print_info "开始执行前端基础URL修复脚本..."

# 获取服务器IP地址或域名
if [ ! -z "$SITE_DOMAIN" ]; then
    SERVER_ADDRESS=$SITE_DOMAIN
    print_info "使用环境变量中的域名: $SERVER_ADDRESS"
else
    # 尝试获取服务器IP，如果无法获取则使用默认值
    SERVER_IP=$(hostname -I | awk '{print $1}')
    if [ -z "$SERVER_IP" ]; then
        print_warning "无法获取服务器IP地址，使用默认值"
        SERVER_IP="localhost"
    fi
    SERVER_ADDRESS=$SERVER_IP
    print_info "使用服务器IP地址: $SERVER_ADDRESS"
fi

# 获取应用端口
PORT=${PORT:-8080}
print_info "使用端口: $PORT"

# 构建基础URL
BASE_URL="http://${SERVER_ADDRESS}:${PORT}/django06g8e/"
print_info "新的基础URL: $BASE_URL"

# 更新http.js文件
HTTP_JS_FILE="templates/front/modules/http/http.js"
if [ -f "$HTTP_JS_FILE" ]; then
    print_info "更新 $HTTP_JS_FILE 中的基础URL..."
    # 创建临时文件进行替换
    sed "s#baseurl = \"http://localhost:8080/django06g8e/\";#baseurl = \"$BASE_URL\";#g" "$HTTP_JS_FILE" > "$HTTP_JS_FILE.tmp"
    sed "s#domain : \"http://localhost:8080/django06g8e/\",#domain : \"$BASE_URL\",#g" "$HTTP_JS_FILE.tmp" > "$HTTP_JS_FILE"
    rm "$HTTP_JS_FILE.tmp"
    print_success "$HTTP_JS_FILE 已更新"
else
    print_error "找不到文件 $HTTP_JS_FILE"
fi

# 更新base.js文件
BASE_JS_FILE="templates/front/admin/src/utils/base.js"
if [ -f "$BASE_JS_FILE" ]; then
    print_info "更新 $BASE_JS_FILE 中的基础URL..."
    # 创建临时文件进行替换
    sed "s#url : \"http://localhost:8080/django06g8e/\",#url : \"$BASE_URL\",#g" "$BASE_JS_FILE" > "$BASE_JS_FILE.tmp"
    sed "s#indexUrl: 'http://localhost:8080/front/index.html'#indexUrl: 'http://${SERVER_ADDRESS}:${PORT}/front/index.html'#g" "$BASE_JS_FILE.tmp" > "$BASE_JS_FILE"
    rm "$BASE_JS_FILE.tmp"
    print_success "$BASE_JS_FILE 已更新"
else
    print_error "找不到文件 $BASE_JS_FILE"
fi

# 更新config.js文件中的adminurl
CONFIG_JS_FILE="templates/front/js/config.js"
if [ -f "$CONFIG_JS_FILE" ]; then
    print_info "更新 $CONFIG_JS_FILE 中的管理员URL..."
    # 创建临时文件进行替换
    sed "s#var adminurl =  \"http://localhost:8080/django06g8e/admin/dist/index.html\";#var adminurl =  \"http://${SERVER_ADDRESS}:${PORT}/django06g8e/admin/dist/index.html\";#g" "$CONFIG_JS_FILE" > "$CONFIG_JS_FILE.tmp"
    mv "$CONFIG_JS_FILE.tmp" "$CONFIG_JS_FILE"
    print_success "$CONFIG_JS_FILE 已更新"
else
    print_error "找不到文件 $CONFIG_JS_FILE"
fi

print_info "检查media目录内容:"
echo "- media/upload/: $(find media/upload -name "*.jpg" 2>/dev/null | wc -l) 个图片文件"
echo "- media/front/: $(find media/front -name "*.jpg" 2>/dev/null | wc -l) 个图片文件"

print_success "前端基础URL修复完成！"
echo ""
print_info "URL修改摘要:"
echo "- 旧URL: http://localhost:8080/django06g8e/"
echo "- 新URL: $BASE_URL"
echo ""
print_info "如果使用容器环境变量，请确保设置了以下环境变量:"
echo "- SITE_DOMAIN: 您的网站域名或IP地址 (可选)"
echo "- PORT: 应用端口号 (可选，默认8080)" 