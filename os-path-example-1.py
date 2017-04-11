'''
os.path 模块包含了许多与平台无关的处理长文件名的函数.
也就是说, 你不需要处理前后斜杠, 冒号等. 
'''

import os

filename = "my/little/pony.txt"
print "using", os.name, "..."
print "split", "=>", os.path.split(filename)
print "splitext", "=>", os.path.splitext(filename)
print "dirname", "=>", os.path.dirname(filename)
print "basename", "=>", os.path.basename(filename)
print "join"," =>", os.path.join(os.path.dirname(filename), os.path.basename(filename))


'''
注意这里的 split 只分割出最后一项(不带斜杠).
os.path 模块中还有许多函数允许你简单快速地获知文件名的一些特征, 如 下例 所示.
'''
FILES = (
    os.curdir,
    "/",
    "file",
    "/file",
    "samples",
    "samples/sample.png",
    "directory/file",
    "../directory/file",
    "/directory/file"
)

for file in FILES:
    print file, "=>",
    if os.path.exists(file):
        print "EXISTS",
    if os.path.isabs(file):
        print "ISABS",
    if os.path.isdir(file):
        print "ISDIR",
    if os.path.isfile(file):
        print "ISFILE",
    if os.path.islink(file):
        print "ISLINK",
    if os.path.ismount(file):
        print "ISMOUNT",
    print