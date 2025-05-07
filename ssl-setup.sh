#!/bin/bash

# 创建SSL证书目录
mkdir -p ssl

# 生成自签名SSL证书
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/craftmarket.key -out ssl/craftmarket.crt \
  -subj "/C=CN/ST=Beijing/L=Beijing/O=CraftMarket Ltd/OU=IT/CN=craftmarket.com" \
  -addext "subjectAltName = DNS:craftmarket.com,DNS:www.craftmarket.com"

echo "自签名SSL证书已生成！"
echo "注意：在生产环境中，应使用受信任的证书颁发机构颁发的证书" 