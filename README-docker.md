# 工艺品交易系统 - Docker部署指南

本文档提供在CentOS上使用Docker部署工艺品交易系统的步骤。

## 先决条件

在CentOS服务器上安装以下软件：

1. Docker
2. Docker Compose

## 安装Docker和Docker Compose

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

## 部署应用

1. 将项目文件复制到服务器

```bash
# 例如使用scp命令
scp -r django06g8e/ user@your-server-ip:/path/to/destination/
```

2. 进入项目目录

```bash
cd /path/to/destination/django06g8e
```

3. 构建并启动容器

```bash
# 开发环境
sudo docker-compose up -d

# 生产环境
sudo docker-compose -f docker-compose-prod.yml up -d
```

4. 等待几分钟让服务启动完成，然后访问:

- 开发环境: http://your-server-ip:8080/admin/dist/index.html
- 生产环境: http://your-server-ip/admin/dist/index.html

## 管理应用

### 查看容器状态

```bash
sudo docker-compose ps
```

### 查看日志

```bash
# 查看所有容器的日志
sudo docker-compose logs

# 查看Web应用的日志
sudo docker-compose logs web
```

### 重启服务

```bash
sudo docker-compose restart
```

### 停止服务

```bash
sudo docker-compose down
```

## 登录信息

系统默认管理员账户:
- 用户名: `admin`
- 密码: `admin`
- 角色: 管理员

## 常见问题

### 数据库连接失败

如果应用无法连接到数据库，可能是因为MySQL容器还没有完全启动。请等待几分钟后再试。

### 端口冲突

如果8080端口已被占用，可以修改`docker-compose.yml`中的端口映射：

```yaml
ports:
  - "8081:8080"  # 将8081改为任何未被使用的端口
```

### 文件权限问题

如果遇到文件权限问题，请确保挂载的卷有正确的权限：

```bash
sudo chown -R 1000:1000 /path/to/destination/django06g8e/media
``` 