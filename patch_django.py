import sys
import re
import os

# Django路径
django_path = '/opt/miniconda3/lib/python3.12/site-packages/django/db/models/fields/__init__.py'

# 读取文件内容
with open(django_path, 'r') as f:
    content = f.read()

# 替换collections.Iterator为collections.abc.Iterator
new_content = re.sub(r'import collections(\n|\r\n)', r'import collections\nimport collections.abc\1', content)
new_content = re.sub(r'collections\.Iterator', r'collections.abc.Iterator', new_content)

# 写回文件
with open(django_path, 'w') as f:
    f.write(new_content)

print('Django field file has been patched successfully!') 