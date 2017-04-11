'''
你可以通过继承 Queue 类来修改它的行为.
下例 为我们展示了一个简单的具有优先级的队列.
它接受一个元组作为参数, 元组的第一个成员表示优先级(数值越小优先级越高).
'''

import Queue
import bisect

Empty = Queue.Empty

class PriorityQueue(Queue.Queue):
    "Thread-safe priority queue"
    #def _init(self, maxsize):
    #    self.queue = []
        
    def _put(self, item):
        # insert in order
        bisect.insort(self.queue, item)
        
    #def _get(self):
    #    return self.queue.pop()[1]    

#
# try it
queue = PriorityQueue(0)

# add items out of order
queue.put((20, "second"))
queue.put((10, "first"))
queue.put((30, "third"))

# print queue contents
try:
    while 1:
        print queue.get_nowait()
except Empty:
    pass


'''
原文的实现似乎有些问题.
这里 PriorityQueue 添加了__init__ 和 _get, 并且在 python 的内置模块中已经实现了 PriorityQueue.
所以这里的实现只是一个展示代码的示例.
'''