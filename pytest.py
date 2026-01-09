# -*- coding: utf-8 -*-
#!/usr/bin/env python3
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

print("="*50)
print("Python环境检查")
print("="*50)
print("当前Python版本: {}".format(sys.version))
print("Python路径: {}".format(sys.executable))

# 检查python3
try:
    python3_path = subprocess.check_output(['which', 'python3'], 
                                          stderr=subprocess.STDOUT).decode().strip()
    print("\npython3路径: {}".format(python3_path))
    
    # 获取python3版本
    python3_version = subprocess.check_output([python3_path, '--version'],
                                            stderr=subprocess.STDOUT).decode().strip()
    print("python3版本: {}".format(python3_version))
except Exception as e:
    print("\npython3未安装或不在PATH中: {}".format(str(e)))

# 列出所有python
print("\n所有可用的python:")
for cmd in ['python', 'python2', 'python3', 'python3.6', 'python3.7', 'python3.8']:
    try:
        path = subprocess.check_output(['which', cmd], 
                                      stderr=subprocess.STDOUT).decode().strip()
        version = subprocess.check_output([path, '--version'],
                                        stderr=subprocess.STDOUT).decode().strip()
        print("  {}: {} -> {}".format(cmd, path, version))
    except Exception as e:
        continue
