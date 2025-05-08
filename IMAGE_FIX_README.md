# 图片显示问题修复指南

本文档解释了工艺品交易系统在Docker环境下图片无法显示的问题及解决方案。

## 问题原因

在Docker容器中运行时，前端代码中的图片URL引用问题是主要原因：

1. 前端代码中的基础URL被硬编码为 `http://localhost:8080/django06g8e/`
2. 当从外部浏览器访问时，"localhost" 指向的是客户端机器而非Docker容器
3. 图片存储在容器的 `/app/media` 目录下，但URL路径构建不正确

## 解决方案

我们提供了两个脚本来解决这个问题：

1. `docker_image_fix.sh` - 确保媒体文件正确复制到media目录
2. `docker_baseurl_fix.sh` - 动态更新前端代码中的基础URL

这些脚本在容器启动时自动运行，使用正确的服务器IP或域名替换硬编码的localhost。

## 使用指南

### 方法一：使用自动检测IP的运行脚本

```bash
# 给脚本添加执行权限
chmod +x run-with-domain.sh

# 运行应用（自动检测服务器IP）
./run-with-domain.sh
```

### 方法二：指定自定义域名或IP

```bash
# 使用特定IP地址
./run-with-domain.sh 192.168.1.100

# 使用域名
./run-with-domain.sh example.com
```

### 方法三：直接设置环境变量

```bash
# 设置环境变量
export SITE_DOMAIN=example.com

# 启动Docker容器
docker-compose up -d --build
```

## 手动调试步骤

如果图片仍然无法显示，您可以尝试以下步骤：

1. 检查媒体文件是否存在：

```bash
docker exec -it django06g8e_web_1 ls -la /app/media/upload
docker exec -it django06g8e_web_1 ls -la /app/media/front
```

2. 手动运行URL修复脚本：

```bash
docker exec -it django06g8e_web_1 bash /app/docker_baseurl_fix.sh
```

3. 检查前端代码中的基础URL：

```bash
docker exec -it django06g8e_web_1 grep -r "baseurl" /app/templates/front/modules/http/http.js
```

4. 在浏览器中打开开发者工具，查看网络请求中图片URL的具体错误

## 技术说明

- 图片文件存储在 `media/upload` 和 `media/front` 目录
- 产品图片路径存储在数据库的 `tupian` 字段中
- 前端通过 `baseurl + item.tupian.split(',')[0]` 构建完整图片URL
- 正确配置需要将 `baseurl` 设置为可从外部访问的服务器地址 