#!/usr/bin/env python
import os
import sys

print("========== 媒体URL配置脚本开始执行 ==========")
print(f"当前工作目录: {os.getcwd()}")

# 要修改的文件
filepath = "dj2/urls.py"
print(f"准备修改文件: {filepath}")

# 检查文件是否存在
if not os.path.exists(filepath):
    print(f"错误: 文件 {filepath} 不存在!")
    sys.exit(1)
else:
    print(f"文件 {filepath} 存在，准备读取内容")

# 读取文件内容
try:
    with open(filepath, 'r') as file:
        content = file.read()
    print(f"成功读取文件 {filepath}, 长度: {len(content)} 字符")
except Exception as e:
    print(f"读取文件时出错: {str(e)}")
    sys.exit(1)

# 导入需要的模块
print("检查是否需要导入MEDIA_ROOT和MEDIA_URL...")
if "from dj2.settings import MEDIA_ROOT" not in content:
    print("需要添加MEDIA_ROOT和MEDIA_URL导入")
    original_content = content
    content = content.replace(
        "from dj2.settings import dbName as schemaName", 
        "from dj2.settings import dbName as schemaName\nfrom dj2.settings import MEDIA_ROOT, MEDIA_URL"
    )
    if original_content == content:
        print("警告: 无法找到合适的位置添加导入语句")
    else:
        print("成功添加MEDIA_ROOT和MEDIA_URL导入")
else:
    print("MEDIA_ROOT和MEDIA_URL导入已存在，无需添加")

# 添加媒体URL配置
print("检查是否需要添加媒体URL配置...")
if "re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})" not in content:
    print("需要添加媒体URL配置")
    
    if "path(r'null',views.null)," in content:
        print("找到插入点: path(r'null',views.null),")
        original_content = content
        content = content.replace(
            "path(r'null',views.null),", 
            "path(r'null',views.null),\n    # 添加媒体文件的URL配置\n    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),"
        )
        if original_content == content:
            print("警告: 替换操作未成功")
        else:
            print("成功在null路径后添加媒体URL配置")
    else:
        print("找不到null路径，尝试在urlpatterns列表末尾添加")
        original_content = content
        content = content.replace(
            "]", 
            "    # 添加媒体文件的URL配置\n    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),\n]"
        )
        if original_content == content:
            print("警告: 在urlpatterns列表末尾添加失败")
        else:
            print("成功在urlpatterns列表末尾添加媒体URL配置")
else:
    print("媒体URL配置已存在，无需添加")

# 写回文件
print(f"将修改后的内容写回 {filepath}...")
try:
    with open(filepath, 'w') as file:
        file.write(content)
    print(f"成功写入文件 {filepath}")
except Exception as e:
    print(f"写入文件时出错: {str(e)}")
    sys.exit(1)

# 检查是否存在必要的导入和配置  
print("验证修改结果...")
with open(filepath, 'r') as file:
    new_content = file.read()
    
if "from dj2.settings import MEDIA_ROOT" in new_content:
    print("MEDIA_ROOT导入存在 ✓")
else:
    print("错误: MEDIA_ROOT导入不存在 ✗")
    
if "re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})" in new_content:
    print("媒体URL配置存在 ✓")
else:
    print("错误: 媒体URL配置不存在 ✗")

# 检查媒体目录权限
print("\n检查媒体目录权限...")
media_dir = "media"
if os.path.exists(media_dir):
    print(f"媒体目录 {media_dir} 存在")
    try:
        os.chmod(media_dir, 0o755)
        print(f"已设置 {media_dir} 目录权限为 755")
        
        # 检查子目录
        for subdir in ["upload", "front"]:
            subdir_path = os.path.join(media_dir, subdir)
            if os.path.exists(subdir_path):
                print(f"子目录 {subdir_path} 存在")
                os.chmod(subdir_path, 0o755)
                print(f"已设置 {subdir_path} 目录权限为 755")
                
                # 列出子目录中的文件数量
                files = [f for f in os.listdir(subdir_path) if f.endswith('.jpg')]
                print(f"{subdir_path} 目录中有 {len(files)} 个jpg文件")
            else:
                print(f"警告: 子目录 {subdir_path} 不存在")
    except Exception as e:
        print(f"设置权限时出错: {str(e)}")
else:
    print(f"警告: 媒体目录 {media_dir} 不存在")

print("========== 媒体URL配置脚本执行完成 ==========") 