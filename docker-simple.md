# 工艺品交易系统 - 简易Docker部署指南

本指南提供简化的Docker部署步骤，让您可以快速部署工艺品交易系统。

## 1. 安装Docker和Docker Compose

在CentOS上安装Docker和Docker Compose:

```bash
# 安装Docker
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce docker-ce-cli containerd.io

# 启动Docker
sudo systemctl start docker
sudo systemctl enable docker

# 安装Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## 2. 部署应用

### 克隆项目并进入目录
```bash
# 将项目复制到服务器上
cd /path/to/your/directory
```

### 运行一键部署脚本
```bash
chmod +x docker-run.sh
./docker-run.sh
```

这个脚本会自动完成:
- 构建Docker镜像
- 启动MySQL和Web服务
- 配置图片资源

## 3. 访问系统

部署完成后，可以通过以下地址访问系统:

- 前台: http://your-server-ip:8080/front/index.html
- 后台: http://your-server-ip:8080/admin/dist/index.html

默认管理员账户:
- 用户名: admin
- 密码: admin

## 4. 常见问题

### 图片无法显示

如果图片不能正常显示，可以手动运行图片修复脚本:

```bash
docker exec -it django06g8e_web_1 python docker_image_fix.sh
```

### 数据库连接问题

如果遇到数据库连接问题，可能需要等待MySQL完全启动:

```bash
# 查看容器状态
docker-compose -f docker-compose-simple.yml ps

# 查看MySQL日志
docker-compose -f docker-compose-simple.yml logs db
```

### 停止服务

要停止服务，运行:

```bash
docker-compose -f docker-compose-simple.yml down
``` 