'''
os 模块也包含了一些用于目录处理的函数.
listdir 函数返回给定目录中所有文件名(包括目录名)组成的列表,
如下例所示. 而 Unix 和 Windows 中使用的当前目录和父目录标记(.和 .. )不包含在此列表中.
'''

import os
for file in os.listdir("samples"):
    print file