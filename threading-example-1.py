'''
注意线程支持模块是可选的, 有可能在一些 Python 解释器中不可用.

执行 Python 程序的时候, 是按照从主模块顶端向下执行的.
循环用于重复执行部分代码, 函数和方法会将控制临时移交到程序的另一部分.
通过线程, 你的程序可以在同时处理多个任务. 每个线程都有它自己的控制流.
所以你可以在一个线程里从文件读取数据, 另个向屏幕输出内容.
为了保证两个线程可以同时访问相同的内部数据, Python 使用了 globalinterpreter lock (全局解释器锁).
在同一时间只可能有一个线程执行Python 代码;
Python 实际上是自动地在一段很短的时间后切换到下个线程执行, 或者等待一个线程执行一项需要时间的操作(例如等待通过 socket 传输的数据, 或是从文件中读取数据).
全局锁事实上并不能避免你程序中的问题.
多个线程尝试访问相同的数据会导致异常状态.

例如以下的代码:

def getitem(key):
    item = cache.get(key)
    if item is None:
        # not in cache; create a new one
        item = create_new_item(key)
        cache[key] = item
    return item
    
    
如果不同的线程先后使用相同的 key 调用这里的 getitem 方法, 那么它们很可能会导致相同的参数调用两次 create_new_item.
大多时候这样做没有问题, 但在某些时候会导致严重错误.
不过你可以使用 lock objects 来同步线程.
一个线程只能拥有一个 lock object, 这样就可以确保某个时刻只有一个线程执行 getitem 函数.
'''

'''
在大多现代操作系统中, 每个程序在它自身的进程( process ) 内执行.
我们通过在 shell 中键入命令或直接在菜单中选择来执行一个程序/进程.
Python 允许你在一个脚本内执行一个新的程序.
大多进程相关函数通过 os 模块定义.
'''

'''
(可选) threading 模块为线程提供了一个高级接口, 如 下例 所示.
它源自 Java 的线程实现.
和低级的 thread 模块相同, 只有你在编译解释器时打开了线程支持才可以使用它 .
你只需要继承 Thread 类, 定义好 run 方法, 就可以创建一 个新的线程.
使用时首先创建该类的一个或多个实例, 然后调用 start 方法.
这样每个实例的 run 方法都会运行在它自己的线程里.
'''

import threading
import time, random

class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0
        
    def increment(self):
        self.lock.acquire() # critical section
        self.value = value = self.value + 1
        self.lock.release()
        return value
    
counter = Counter()

class Worker(threading.Thread):
    #def __init__(self):
    #    threading.Thread.__init__(self)
        
    def run(self):
        for i in range(10):
            # pretend we're doing something that takes 10?00 ms
            value = counter.increment() # increment global counter
            time.sleep(random.randint(10, 100) / 1000.0)
            print self.getName(), "-- task", i, "finished", value

#
# try it
for i in range(10):
    Worker().start() # start a worker