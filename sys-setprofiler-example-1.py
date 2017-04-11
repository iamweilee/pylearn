'''
setprofiler 函数允许你配置一个分析函数(profiling function).
这个函数会在每次调用某个函数或方法时被调用(明确或隐含的), 或是遇到异常的时候被调用. 
'''

import sys

def test(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

def profiler(frame, event, arg):
    print event, frame.f_code.co_name, frame.f_lineno, "->", arg
    
# profiler is activated on the next call, return, or exception
# 分析函数将在下次函数调用, 返回, 或异常时激活
sys.setprofile(profiler)

# profile this function call
# 分析这次函数调用
test(1)

# disable profiler
# 禁用分析函数
sys.setprofile(None)

# don't profile this call
# 不会分析这次函数调用
test(2)


'''
基于该函数, profile 模块提供了一个完整的分析器框架.
'''