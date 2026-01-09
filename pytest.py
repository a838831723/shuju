# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os

def ensure_python3():
    """确保脚本使用Python 3执行"""
    if sys.version_info[0] < 3:
        # Python 2环境，切换到Python 3
        python3_path = '/bin/python3'
        current_script = os.path.abspath(__file__)
        
        print(f"当前是Python {sys.version_info[0]}.{sys.version_info[1]}，正在切换到Python 3...")
        
        # 重建环境变量
        env = os.environ.copy()
        env['PYTHON_LAUNCHER'] = python3_path
        
        # 用Python 3重新执行当前脚本
        os.execve(python3_path, [python3_path, current_script] + sys.argv[1:], env)
        # 如果execve失败
        print("切换到Python 3失败")
        sys.exit(1)

# 确保使用Python 3
ensure_python3()

# ===================== 以下是你的实际代码 =====================
print("✓ 成功使用Python 3执行!")
print(f"Python版本: {sys.version}")
print(f"Python路径: {sys.executable}")

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
