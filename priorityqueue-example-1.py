'''
���� Ϊ����չʾ�� PriorityQueue ��ʹ��.
�������ΪԪ��, Ԫ��ĵ�һ����Ա��ʾ���ȼ�(��ֵԽС���ȼ�Խ��).
�������Ϊ���ֻ��ַ���, ����������ĸ��ASCII������, ֵԽС���ȼ�Խ��.
'''

import Queue
import bisect

Empty = Queue.Empty

#
# try it
queue = Queue.PriorityQueue(0)

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