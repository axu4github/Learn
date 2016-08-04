# -*- coding: UTF-8 -*-

import psutil


print psutil.virtual_memory()
print psutil.virtual_memory().total / (1024 * 1024 * 1024)
print psutil.swap_memory()
print psutil.cpu_count(logical=False)
print psutil.cpu_count()
