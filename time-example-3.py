'''
在一些平台上, time 模块包含了 strptime 函数, 它的作用与 strftime 相反.
给定一个字符串和模式, 它返回相应的时间对象, 如 下例 所示.
'''

import time

# make sure we have a strptime function!
# 确认有函数 strptime
try:
    strptime = time.strptime
except AttributeError:
    from strptime import strptime
    
print strptime("30 Nov 00", "%d %b %y")
print strptime("1 Jan 70 1:30pm", "%d %b %y %I:%M%p")

'''
只有在系统的 C 库提供了相应的函数的时候, time.strptime 函数才可以使用.
对于没有提供标准实现的平台, strptime.py 提供了一个不完全的实现.
'''