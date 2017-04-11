'''
fork 和 wait 函数在 Windows 上是不可用的, 但是你可以使用 spawn 函数,
如 下例 所示. 不过, spawn 不会沿着路径搜索可执行文件, 你必须自己处理好这些.
'''

import os
import string

def run(program, *args):
    # find executable
    for path in string.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(os.P_WAIT, file, (file,) + args)
        except os.error:
            pass
        #raise os.error, "cannot find executable"
    

run("python", "hello.py")
print "goodbye"