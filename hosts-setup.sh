#!/bin/bash

# 该脚本用于在本地开发环境中设置hosts文件，使craftmarket.com指向本地

# 检查是否有root权限
if [ "$(id -u)" != "0" ]; then
   echo "此脚本需要root权限才能修改hosts文件"
   echo "请使用sudo运行此脚本"
   exit 1
fi

# 检查hosts文件
HOSTS_FILE="/etc/hosts"
DOMAIN="craftmarket.com"
DOMAIN_ENTRY="127.0.0.1 craftmarket.com www.craftmarket.com"

# 检查域名是否已存在于hosts文件中
if grep -q "$DOMAIN" "$HOSTS_FILE"; then
    echo "$DOMAIN 已存在于hosts文件中，无需更改"
else
    # 添加域名到hosts文件
    echo "$DOMAIN_ENTRY" >> "$HOSTS_FILE"
    echo "已将 $DOMAIN 添加到hosts文件"
fi

echo "设置完成！您现在可以通过以下地址访问您的应用："
echo "http://craftmarket.com"
echo "http://www.craftmarket.com" 