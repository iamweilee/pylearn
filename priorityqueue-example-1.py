'''
下例 为我们展示了 PriorityQueue 的使用.
如果参数为元组, 元组的第一个成员表示优先级(数值越小优先级越高).
如果参数为数字或字符串, 则按照数字字母的ASCII码排序, 值越小优先级越高.
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