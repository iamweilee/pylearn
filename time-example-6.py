'''
time 模块可以计算 Python 程序的执行时间, 如 下例 所示.
你可以测量 "wall time" (real world time), 或是"进程时间" (消耗的 CPU 时间).
'''

import time

def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"

'''
并不是所有的系统都能测量真实的进程时间. 一些系统中(包括 Windows ), clock 函数通常测量从程序启动到测量时的 wall time.
进程时间的精度受限制. 在一些系统中, 它超过 30 分钟后进程会被清理.
(原文: On many systems, it wraps around after just over 30 minutes.)
另参见 timing 模块( Windows 下的朋友不用忙活了,没有地~), 它可以测量两个事件之间的 wall time.
'''