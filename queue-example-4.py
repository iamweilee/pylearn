'''
���� չʾ��һ���򵥵Ķ�ջ (stack) ʵ�� (ĩβ���, ͷ������, ����ͷ�����, ͷ������).
Ҳ���� LifoQueue ��, ��ʵ python Ҳ�����˸�ģ���ʵ��.
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