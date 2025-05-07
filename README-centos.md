# 工艺品交易系统 - CentOS部署指南

本文档提供在CentOS服务器上部署工艺品交易系统的详细步骤。

## 一、系统要求

- CentOS 7或更高版本
- 至少2GB内存
- 至少20GB磁盘空间
- 具有root权限的用户账号

## 二、一键部署（推荐）

我们提供了一键部署脚本，可以自动完成环境配置、应用部署等操作。

### 步骤：

1. 将整个项目目录上传到CentOS服务器

```bash
# 示例：使用scp命令从本地上传
scp -r django06g8e/ user@your-server-ip:/home/user/
```

2. 登录服务器并进入项目目录

```bash
ssh user@your-server-ip
cd /home/user/django06g8e/
```

3. 执行一键部署脚本

```bash
# 给脚本添加执行权限
chmod +x one-click-deploy.sh

# 以root权限运行脚本
sudo ./one-click-deploy.sh
```

4. 等待部署完成

脚本会自动完成以下操作：
- 安装Docker和Docker Compose（如果未安装）
- 创建媒体目录并准备图片资源
- 创建Docker配置文件
- 构建并启动Docker容器

5. 访问系统

部署完成后，可以通过以下地址访问系统：
- 前台：`http://服务器IP:8080/front/index.html`
- 后台：`http://服务器IP:8080/admin/dist/index.html`

默认管理员账号：
- 用户名：`admin`
- 密码：`admin`

## 三、手动部署

如果您希望手动部署系统，请按照以下步骤操作：

### 1. 安装Docker

```bash
# 安装必要的依赖
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

# 添加Docker仓库
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# 安装Docker
sudo yum install -y docker-ce docker-ce-cli containerd.io

# 启动Docker并设置开机自启
sudo systemctl start docker
sudo systemctl enable docker
```

### 2. 安装Docker Compose

```bash
# 下载Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 添加执行权限
sudo chmod +x /usr/local/bin/docker-compose

# 创建软链接
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

### 3. 准备应用环境

```bash
# 进入项目目录
cd /path/to/django06g8e

# 创建必要的目录
mkdir -p media/upload
mkdir -p media/front

# 准备图片资源
cp -r templates/front/*.jpg media/upload/ 2>/dev/null || true
cp -r templates/front/*.jpg media/front/ 2>/dev/null || true

# 执行图片修复脚本
chmod +x docker_image_fix.sh
./docker_image_fix.sh
```

### 4. 构建并启动容器

```bash
# 构建并启动容器
docker-compose up -d --build
```

### 5. 验证部署

```bash
# 检查容器状态
docker-compose ps
```

## 四、常见问题

### 1. 图片无法显示

如果前端页面的图片无法正常显示，可以手动运行图片修复脚本：

```bash
docker exec -it django06g8e_web_1 bash /app/docker_image_fix.sh
```

### 2. 端口被占用

如果8080端口被占用，可以修改`docker-compose.yml`文件中的端口映射配置：

```yaml
ports:
  - "新端口:8080"
```

然后重启容器：

```bash
docker-compose down
docker-compose up -d
```

### 3. 数据库连接问题

如果遇到数据库连接问题，可以查看日志并等待MySQL容器完全启动：

```bash
docker-compose logs db
docker-compose logs web
``` 