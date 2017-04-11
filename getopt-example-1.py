'''
getopt 模块包含用于抽出命令行选项和参数的函数, 它可以处理多种格式的选项.
如 下图 所示.
其中第 2 个参数指定了允许的可缩写的选项. 选项名后的冒号(:) 意味着这个选项必须有额外的参数.
'''

import getopt
import sys

# simulate command-line invocation
# 模仿命令行参数
sys.argv = ["myscript.py", "-l", "-d", "directory", "filename"]

# process options
# 处理选项
opts, args = getopt.getopt(sys.argv[1:], "ld:")
long = 0
directory = None

for o, v in opts:
    if o == "-l":
        long = 1
    elif o == "-d":
        directory = v

print "long", "=", long
print "directory", "=", directory
print "arguments", "=", args