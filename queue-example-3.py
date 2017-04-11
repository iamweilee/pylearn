'''
�����ͨ���̳� Queue �����޸�������Ϊ.
���� Ϊ����չʾ��һ���򵥵ľ������ȼ��Ķ���.
������һ��Ԫ����Ϊ����, Ԫ��ĵ�һ����Ա��ʾ���ȼ�(��ֵԽС���ȼ�Խ��).
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
ԭ�ĵ�ʵ���ƺ���Щ����.
���� PriorityQueue �����__init__ �� _get, ������ python ������ģ�����Ѿ�ʵ���� PriorityQueue.
���������ʵ��ֻ��һ��չʾ�����ʾ��.
'''