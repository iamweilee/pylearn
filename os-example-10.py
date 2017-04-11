'''
需要创建一个真正的后台程序稍微有点复杂, 首先调用 setpgrp 函数创建一个"进程组首领/process group leader".
否则, 向无关进程组发送的信号(同时)会引起守护进程的问题:

os.setpgrp()

为了确保守护进程创建的文件能够获得程序指定的 mode flags(权限模式标记?), 最好删除 user mode mask:

os.umask(0)

然后, 你应该重定向 stdout/stderr 文件, 而不能只是简单地关闭它们(如果你的程序需要 stdout 或 stderr 写入内容的时候, 可能会出现意想不到的问题).

class NullDevice:
    def write(self, s):
        pass
sys.stdin.close()
sys.stdout = NullDevice()
sys.stderr = NullDevice()

换言之, 由于 Python 的 print 和 C 中的 printf/fprintf 在设备(device)
没有连接后不会关闭你的程序, 此时守护进程中的 sys.stdout.write() 会抛
出一个 IOError 异常, 而你的程序依然在后台运行的很好....
另外, 先前例子中的 _exit 函数会终止当前进程. 而 sys.exit 不同, 如果调
用者(caller) 捕获了 SystemExit 异常, 程序仍然会继续执行. 如 下例 所示.
'''

import os
import sys
try:
    sys.exit(1)
except SystemExit, value:
    print "caught exit(%s)" % value
try:
    os._exit(2)
except SystemExit, value:
    print "caught exit(%s)" % value
    
print "bye!"