'''
time 模块提供了一些处理日期和一天内时间的函数. 它是建立在 C 运行时库的简单封装.
给定的日期和时间可以被表示为浮点型(从参考时间, 通常是 1970.1.1 到现在经过的秒数. 即 Unix 格式), 或者一个表示时间的 struct (类元组).
下例展示了如何使用 time 模块获取当前时间.
'''

import time

now = time.time()

print now, "seconds since", time.gmtime(0)[:6]
print
print "or in other words:"
print "- local time:", time.localtime(now)
print "- utc:", time.gmtime(now)

'''
localtime 和 gmtime 返回的类元组包括年, 月, 日, 时, 分, 秒, 星期, 一年的第几天, 日光标志.
其中年是一个四位数(在有千年虫问题的平台上另有规定, 但还是四位数), 星期从星期一(数字 0 代表)开始, 1 月 1 日是一年的第一天.
'''