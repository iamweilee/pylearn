'''
setprofiler ��������������һ����������(profiling function).
�����������ÿ�ε���ĳ�������򷽷�ʱ������(��ȷ��������), ���������쳣��ʱ�򱻵���. 
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
# �������������´κ�������, ����, ���쳣ʱ����
sys.setprofile(profiler)

# profile this function call
# ������κ�������
test(1)

# disable profiler
# ���÷�������
sys.setprofile(None)

# don't profile this call
# ���������κ�������
test(2)


'''
���ڸú���, profile ģ���ṩ��һ�������ķ��������.
'''