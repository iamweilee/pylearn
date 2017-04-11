'''
���� �е� settrace �����������, ���� trace �������ڽ�����ÿִ�е��µ�һ��ʱ������.
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
# �����������´κ�������, ����, ���쳣ʱ����
sys.settrace(tracer)

# trace this function call
# ������κ�������
test(1)

# disable tracing
# ���ø�����
sys.settrace(None)

# don't trace this call
# ���������κ�������
test(2)

'''
���ڸú����ṩ�ĸ��ٹ���, pdb ģ���ṩ�������ĵ���( debug )���.
'''