'''
将时间元组转换回时间值非常简单, 至少我们谈论的当地时间 (local time) 如此.
只要把时间元组传递给 mktime 函数, 如 下例 所示.
'''

import time

t0 = time.time()
tm = time.localtime(t0)

print tm
print t0
print time.mktime(tm)