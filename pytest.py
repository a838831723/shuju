# -*- coding: utf-8 -*-
import sys
print(sys.version.split()[0])
print(sys.executable)
import os
for key, value in sorted(os.environ.items()):
    print(key = value)
print(os.environ)
