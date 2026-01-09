# -*- coding: utf-8 -*-
import sys
print(sys.version.split()[0])
print(sys.executable)
import os
for key, value in sorted(os.environ.items()):
    print(key , value)
print(os.environ)


import sys
import os
import subprocess

print("当前Python版本:", sys.version)

# 检查python3是否在PATH中
print("\n检查python3是否存在:")
try:
    # 方法1：使用which命令
    result = subprocess.check_output(['which', 'python3'], stderr=subprocess.STDOUT)
    print("python3路径:", result.decode().strip())
except subprocess.CalledProcessError:
    print("python3未找到")

# 方法2：遍历PATH查找
print("\n在PATH中查找python相关程序:")
for path in os.environ.get('PATH', '').split(':'):
    if os.path.exists(path):
        for f in os.listdir(path):
            if 'python' in f:
                full_path = os.path.join(path, f)
                if os.access(full_path, os.X_OK):
                    print(f"  {full_path}")
