'''
但是, 1.5.2 版本的标准库没有提供能将 UTC 时间 (Universal Time, Coordinated: 特林威治标准时间)转换为时间值的函数 ( Python 和对应底层 C 库都没有提供).
下例中 提供了该函数的一个 Python 实现, 称为timegm .
'''

import time

def _d(y, m, d, days=(0,31,59,90,120,151,181,212,243,273,304,334,365)):
    # map a date to the number of days from a reference point
    return (((y - 1901)*1461)/4 + days[m-1] + d + ((m > 2 and not y % 4 and (y % 100 or not y % 400)) and 1))

def timegm(tm, epoch=_d(1970,1,1)):
    year, month, day, h, m, s = tm[:6]
    assert year >= 1970
    assert 1 <= month <= 12
    return (_d(year, month, day) - epoch)*86400 + h*3600 + m*60 + s


t0 = time.time()
tm = time.gmtime(t0)

print tm

print t0
print timegm(tm)

'''
从 1.6 版本开始, calendar 模块提供了一个类似的函数 calendar.timegm .
'''