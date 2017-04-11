'''
下例 展示了一个简单的堆栈 (stack) 实现 (末尾添加, 头部弹出, 而非头部添加, 头部弹出).
也就是 LifoQueue 类, 其实 python 也内置了该模块的实现.
'''

import Queue

Empty = Queue.Empty

class Stack(Queue.Queue):
    "Thread-safe stack"   
    def _put(self, item):
        # insert at the beginning of queue, not at the end
        self.queue.insert(0, item)
        
    # method aliases
    push = Queue.Queue.put
    pop = Queue.Queue.get
    pop_nowait = Queue.Queue.get_nowait
    
    
#
# try it
stack = Stack(0)

# push items on stack
stack.push("first")
stack.push("second")
stack.push("third")

# print stack contents
try:
    while 1:
        print stack.pop_nowait()
except Empty:
    pass