'''
Python 还提供了 execfile 函数, 一个从文件加载代码, 编译代码, 执行代码的快捷方式.
下例 简单地展示了如何使用这个函数.
'''

execfile("hello.py")

def EXECFILE(filename, locals=None, globals=None):
    exec compile(open(filename).read(), filename, "exec") in locals, globals
    
EXECFILE("hello.py")