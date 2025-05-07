import collections
import collections.abc

# 将collections.abc中的Iterator添加到collections模块
if not hasattr(collections, 'Iterator'):
    collections.Iterator = collections.abc.Iterator

# 应用补丁
print("Collections patch applied successfully.") 