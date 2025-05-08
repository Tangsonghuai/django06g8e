#!/usr/bin/env python
import os
import sys
from pathlib import Path

print("========== 媒体文件服务调试脚本开始执行 ==========")

# 检查当前工作目录
base_dir = os.getcwd()
print(f"当前工作目录: {base_dir}")

# 检查Django设置文件
settings_path = os.path.join(base_dir, "dj2", "settings.py")
print(f"检查Django设置文件: {settings_path}")

if not os.path.exists(settings_path):
    print(f"错误: Django设置文件不存在: {settings_path}")
    sys.exit(1)

# 解析设置文件中的媒体配置
try:
    with open(settings_path, 'r') as f:
        settings_content = f.read()
        print("成功读取设置文件")
        
        # 提取MEDIA_URL和MEDIA_ROOT
        media_url_line = next((line for line in settings_content.splitlines() if "MEDIA_URL" in line), None)
        media_root_line = next((line for line in settings_content.splitlines() if "MEDIA_ROOT" in line), None)
        
        if media_url_line:
            print(f"MEDIA_URL 设置: {media_url_line.strip()}")
        else:
            print("警告: 未找到MEDIA_URL设置")
            
        if media_root_line:
            print(f"MEDIA_ROOT 设置: {media_root_line.strip()}")
        else:
            print("警告: 未找到MEDIA_ROOT设置")
except Exception as e:
    print(f"读取设置文件时出错: {str(e)}")

# 检查URL配置
urls_path = os.path.join(base_dir, "dj2", "urls.py")
print(f"\n检查URL配置文件: {urls_path}")

if not os.path.exists(urls_path):
    print(f"错误: URL配置文件不存在: {urls_path}")
    sys.exit(1)

try:
    with open(urls_path, 'r') as f:
        urls_content = f.read()
        print("成功读取URL配置文件")
        
        # 检查是否导入了serve和媒体设置
        if "from django.views.static import serve" in urls_content:
            print("static.serve 导入存在 ✓")
        else:
            print("错误: static.serve 导入不存在 ✗")
            
        if "from dj2.settings import MEDIA_ROOT" in urls_content:
            print("MEDIA_ROOT 导入存在 ✓")
        else:
            print("错误: MEDIA_ROOT 导入不存在 ✗")
            
        # 检查媒体URL配置
        if "re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})" in urls_content:
            print("媒体URL配置存在 ✓")
        else:
            print("错误: 媒体URL配置不存在 ✗")
except Exception as e:
    print(f"读取URL配置文件时出错: {str(e)}")

# 检查媒体目录和文件
media_dir = os.path.join(base_dir, "media")
print(f"\n检查媒体目录: {media_dir}")

if os.path.exists(media_dir):
    print(f"媒体目录存在 ✓")
    
    # 检查权限
    stat_info = os.stat(media_dir)
    print(f"媒体目录权限: {oct(stat_info.st_mode)[-3:]}")
    
    # 检查子目录
    for subdir in ["upload", "front"]:
        subdir_path = os.path.join(media_dir, subdir)
        if os.path.exists(subdir_path):
            print(f"子目录 {subdir} 存在 ✓")
            
            # 检查权限
            subdir_stat = os.stat(subdir_path)
            print(f"子目录 {subdir} 权限: {oct(subdir_stat.st_mode)[-3:]}")
            
            # 列出子目录中的文件
            files = [f for f in os.listdir(subdir_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            print(f"子目录 {subdir} 中有 {len(files)} 个图片文件")
            
            if files:
                print(f"示例文件: {', '.join(files[:3])}")
                
                # 选择第一个文件检查
                sample_file = os.path.join(subdir_path, files[0])
                sample_stat = os.stat(sample_file)
                print(f"示例文件 {files[0]} 权限: {oct(sample_stat.st_mode)[-3:]}")
                print(f"示例文件 {files[0]} 大小: {sample_stat.st_size} 字节")
        else:
            print(f"错误: 子目录 {subdir} 不存在 ✗")
else:
    print(f"错误: 媒体目录不存在 ✗")

# 检查容器环境
if os.path.exists("/.dockerenv"):
    print("\n检测到Docker容器环境")
    
    # 检查启动脚本
    start_script = os.path.join(base_dir, "start.sh")
    if os.path.exists(start_script):
        print(f"启动脚本存在: {start_script} ✓")
        
        try:
            with open(start_script, 'r') as f:
                start_content = f.read()
                print(f"启动脚本内容长度: {len(start_content)} 字符")
                
                # 检查关键设置
                if "chmod -R 755 /app/media" in start_content:
                    print("启动脚本包含媒体目录权限设置 ✓")
                else:
                    print("警告: 启动脚本未包含媒体目录权限设置")
        except Exception as e:
            print(f"读取启动脚本时出错: {str(e)}")
    else:
        print(f"警告: 启动脚本不存在: {start_script}")
else:
    print("\n当前不在Docker容器环境中")

print("\n总结:")
print("1. 创建一个测试媒体文件访问URL")
print("   - 根据典型图片路径，访问URL应该是: /media/front/背景.jpg")
print("2. 检查浏览器网络请求，确认是否有404错误")
print("3. 监控Django日志，查看媒体文件请求处理情况")

print("\n建议:")
print("1. 确保urls.py中正确配置了媒体文件URL路径")
print("2. 确保媒体文件目录权限为755")
print("3. 重启Django服务器，刷新浏览器缓存")
print("4. 检查Django DEBUG设置是否启用")

print("========== 媒体文件服务调试脚本执行完成 ==========") 