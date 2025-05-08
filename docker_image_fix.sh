#!/bin/bash

# 图片修复脚本：解决Docker容器中图片无法显示的问题
# 适用于CentOS和其他Linux发行版

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

print_info "开始执行图片修复脚本..."

# 1. 检查templates目录是否存在
if [ ! -d "templates/front" ]; then
    print_error "templates/front目录不存在！请确保您在项目根目录下运行此脚本。"
    exit 1
fi

# 2. 创建需要的目录结构
print_info "创建媒体目录结构..."
mkdir -p media/upload
mkdir -p media/front

if [ ! -d "media/upload" ] || [ ! -d "media/front" ]; then
    print_error "无法创建media目录，请检查权限。"
    exit 1
fi

# 3. 将templates/front下的图片文件复制到media/upload和media/front目录
print_info "复制图片文件到media目录..."
cp -r templates/front/*.jpg media/upload/ 2>/dev/null || true
cp -r templates/front/*.jpg media/front/ 2>/dev/null || true

# 检查是否有图片文件复制成功
if [ ! "$(ls -A media/upload/ 2>/dev/null)" ]; then
    print_warning "警告: media/upload/目录为空，可能没有找到jpg图片文件。"
fi

# 4. 创建特定的图片占位符（图片名称基于服务器日志）
print_info "创建必要的图片占位符..."

# 保存一张背景图作为默认图片
if [ -f "templates/front/背景.jpg" ]; then
    cp -f templates/front/背景.jpg media/upload/background.jpg 2>/dev/null || true
    cp -f templates/front/背景.jpg media/front/background.jpg 2>/dev/null || true
else
    # 如果没有找到背景.jpg，使用任何可用的第一张jpg
    FIRST_JPG=$(ls templates/front/*.jpg 2>/dev/null | head -1)
    if [ -n "$FIRST_JPG" ]; then
        cp -f "$FIRST_JPG" media/upload/background.jpg 2>/dev/null || true
        cp -f "$FIRST_JPG" media/front/background.jpg 2>/dev/null || true
        print_info "使用 $FIRST_JPG 作为默认背景图"
    else
        print_error "没有找到任何jpg图片文件！"
    fi
fi

# 创建新闻图片
print_info "创建新闻图片占位符..."
for i in $(seq 1 8); do
  if [ -f "templates/front/背景.jpg" ]; then
    cp -f templates/front/背景.jpg media/upload/news_picture${i}.jpg 2>/dev/null || true
    cp -f templates/front/背景.jpg media/front/news_picture${i}.jpg 2>/dev/null || true
  elif [ -n "$FIRST_JPG" ]; then
    cp -f "$FIRST_JPG" media/upload/news_picture${i}.jpg 2>/dev/null || true
    cp -f "$FIRST_JPG" media/front/news_picture${i}.jpg 2>/dev/null || true
  fi
done

# 创建商品图片
print_info "创建商品图片占位符..."
for i in $(seq 1 8); do
  if [ -f "templates/front/木篮子.jpg" ]; then
    cp -f templates/front/木篮子.jpg media/upload/shangpinxinxi_tupian${i}.jpg 2>/dev/null || true
    cp -f templates/front/木篮子.jpg media/front/shangpinxinxi_tupian${i}.jpg 2>/dev/null || true
  elif [ -n "$FIRST_JPG" ]; then
    cp -f "$FIRST_JPG" media/upload/shangpinxinxi_tupian${i}.jpg 2>/dev/null || true
    cp -f "$FIRST_JPG" media/front/shangpinxinxi_tupian${i}.jpg 2>/dev/null || true
  fi
done

# 创建公告图片
print_info "创建公告图片占位符..."
for i in $(seq 1 8); do
  if [ -f "templates/front/背景2.jpg" ]; then
    cp -f templates/front/背景2.jpg media/upload/gonggaoxinxi_tupian${i}.jpg 2>/dev/null || true
    cp -f templates/front/背景2.jpg media/front/gonggaoxinxi_tupian${i}.jpg 2>/dev/null || true
  elif [ -f "templates/front/背景.jpg" ]; then
    cp -f templates/front/背景.jpg media/upload/gonggaoxinxi_tupian${i}.jpg 2>/dev/null || true
    cp -f templates/front/背景.jpg media/front/gonggaoxinxi_tupian${i}.jpg 2>/dev/null || true
  elif [ -n "$FIRST_JPG" ]; then
    cp -f "$FIRST_JPG" media/upload/gonggaoxinxi_tupian${i}.jpg 2>/dev/null || true
    cp -f "$FIRST_JPG" media/front/gonggaoxinxi_tupian${i}.jpg 2>/dev/null || true
  fi
done

# 创建其他常用图片
print_info "创建其他通用图片占位符..."
for i in $(seq 1 3); do
  if [ -f "templates/front/背景${i}.jpg" ]; then
    cp -f templates/front/背景${i}.jpg media/upload/picture${i}.jpg 2>/dev/null || true
    cp -f templates/front/背景${i}.jpg media/front/picture${i}.jpg 2>/dev/null || true
  elif [ -f "templates/front/背景.jpg" ]; then
    cp -f templates/front/背景.jpg media/upload/picture${i}.jpg 2>/dev/null || true
    cp -f templates/front/背景.jpg media/front/picture${i}.jpg 2>/dev/null || true
  elif [ -n "$FIRST_JPG" ]; then
    cp -f "$FIRST_JPG" media/upload/picture${i}.jpg 2>/dev/null || true
    cp -f "$FIRST_JPG" media/front/picture${i}.jpg 2>/dev/null || true
  fi
done

# 4. 修复权限
print_info "修复文件权限..."
chmod -R 755 media

# 5. 检查处理结果
if [ "$(find media/upload -name "*.jpg" | wc -l)" -gt 0 ] && [ "$(find media/front -name "*.jpg" | wc -l)" -gt 0 ]; then
    print_success "图片修复完成！"
    echo ""
    print_info "已创建以下目录和文件:"
    echo "- media/upload/: $(find media/upload -name "*.jpg" | wc -l) 个图片文件"
    echo "- media/front/: $(find media/front -name "*.jpg" | wc -l) 个图片文件"
    echo ""
    print_info "注意：请确保Docker容器中配置了以下卷映射："
    echo "- ./media:/app/media"
else
    print_error "图片修复可能未成功完成。请检查日志。"
fi

# 6. 导入SQL数据
if [ -f "db/django06g8e.sql" ]; then
    print_info "正在导入数据库SQL文件..."
    # 在容器内执行时，使用容器内的数据库配置
    if [ -f "/.dockerenv" ]; then
        mysql -h db -u root -proot_password django06g8e < db/django06g8e.sql
        if [ $? -eq 0 ]; then
            print_success "SQL数据导入完成！"
        else
            print_error "SQL数据导入失败！请检查日志和数据库连接。"
        fi
    else
        print_warning "当前不在Docker容器内，跳过SQL导入步骤。"
    fi
else
    print_error "找不到SQL文件：db/django06g8e.sql"
fi 