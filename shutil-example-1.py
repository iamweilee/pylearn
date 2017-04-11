'''
shutil 实用模块包含了一些用于复制文件和文件夹的函数.
下例 中使用的 copy 函数使用和 Unix 下 cp 命令基本相同的方式复制一个文件.
'''

import shutil
import os

for file in os.listdir("."):
    if os.path.splitext(file)[1] == ".py":
        print file
        shutil.copy(file, os.path.join("backup", file))