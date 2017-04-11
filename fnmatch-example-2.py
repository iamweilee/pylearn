'''
下例 中的 translate 函数可以将一个文件匹配模式转换为正则表达式.
'''

import fnmatch
import os, re

pattern = fnmatch.translate("*.png")

for file in os.listdir("samples"):
    if re.match(pattern, file):
        print file

print "(pattern was %s)" % pattern

'''
glob 和 find 模块在内部使用 fnmatch 模块来实现.
'''