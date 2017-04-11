'''
exec 函数会使用新进程替换当前进程(或者说是"转到进程").
在下例中, 字符串 "goodbye" 永远不会被打印.
'''

import os
import sys

program = "python"
arguments = ["hello.py"]

print os.execvp(program, (program,) + tuple(arguments))
print "goodbye"


'''
Python 提供了很多表现不同的 exec 函数.
上例中使用的是 execvp 函数, 它会从标准路径搜索执行程序, 把第二个参数(元组)作为单独的参数传递给程序, 并使用当前的环境变量来运行程序.
其他七个同类型函数请参阅 Python Library Reference .
'''