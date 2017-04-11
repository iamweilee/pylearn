'''
在 Unix 环境下, 你可以通过组合使用 exec , fork 以及 wait 函数来从当前
程序调用另一个程序, 如 下例 所示. fork 函数复制当前进程, wait
函数会等待一个子进程执行结束.
'''

import os
import sys

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) + args)
    return os.wait()[0]


run("python", "hello.py")
print "goodbye"


'''
fork 函数在子进程返回中返回 0 (这个进程首先从 fork 返回值), 在父进程中返回一个非 0 的进程标识符(子进程的 PID ).
也就是说, 只有当我们处于子进程的时候 "not pid " 才为真.
'''