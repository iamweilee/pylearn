'''
下例 中的 settrace 函数与此类似, 但是 trace 函数会在解释器每执行到新的一行时被调用.
'''

import sys

def test(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

def tracer(frame, event, arg):
    print event, frame.f_code.co_name, frame.f_lineno, "->", arg
    return tracer

# tracer is activated on the next call, return, or exception
# 跟踪器将在下次函数调用, 返回, 或异常时激活
sys.settrace(tracer)

# trace this function call
# 跟踪这次函数调用
test(1)

# disable tracing
# 禁用跟踪器
sys.settrace(None)

# don't trace this call
# 不会跟踪这次函数调用
test(2)

'''
基于该函数提供的跟踪功能, pdb 模块提供了完整的调试( debug )框架.
'''