'''
(可选) thread 模块提为线程提供了一个低级 (low_level) 的接口, 如 下例 所示.
只有你在编译解释器时打开了线程支持才可以使用它.
如果没有特殊需要, 最好使用高级接口 threading 模块替代.
'''

import thread
import time, random

def worker():
    for i in range(50):
        # pretend we're doing something that takes 10?00 ms
        time.sleep(random.randint(10, 100) / 1000.0)
        print thread.get_ident(), "-- task", i, "finished"
        
#
# try it out!
for i in range(2):
    thread.start_new_thread(worker, ())

time.sleep(1)

print "goodbye!"


'''
注意当主程序退出的时候, 所有的线程也随着退出.
而 threading 模块不存在这个问题 . (该行为可改变)
'''