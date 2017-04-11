'''
Queue 模块提供了一个线程安全的队列 (queue) 实现, 如 下例 所示.
你可以通过它在多个线程里安全访问同个对象.
'''

import threading
import Queue
import time, random

WORKERS = 2

class Worker(threading.Thread):
    
    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            item = self.__queue.get()
            if item is None:
                break # reached end of queue
            
            # pretend we're doing something that takes 10?00 ms
            time.sleep(random.randint(10, 100) / 1000.0)
            
            print "task", item, "finished"
#
# try it
queue = Queue.Queue(0)

for i in range(WORKERS):
    Worker(queue).start() # start a worker
   
for i in range(10):
    queue.put(i)
     
for i in range(WORKERS):
    queue.put(None) # add end-of-queue markers