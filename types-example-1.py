'''
types ģ������˱�׼������������������͵����Ͷ���, �� ���� ��ʾ.
ͬһ���͵����ж�����һ�����Ͷ���. �����ʹ�� is �����һ�������ǲ�������ĳ����������.
'''

import types

def check(object):
    print object,
    if type(object) is types.IntType:
        print "INTEGER",
    if type(object) is types.FloatType:
        print "FLOAT",
    if type(object) is types.StringType:
        print "STRING",
    if type(object) is types.ClassType:
        print "CLASS",
    if type(object) is types.InstanceType:
        print "INSTANCE",
    print
    
    
check(0)
check(0.0)
check("0")

class A:
    pass

class B:
    pass

check(A)
check(B)

a = A()
b = B()

check(a)
check(b)


'''
ע�����е��඼������ͬ������, ���е�ʵ��Ҳ��һ��.
Ҫ����һ�������ʵ����������, ����ʹ���ڽ��� issubclass �� isinstance ����.
types ģ���ڵ�һ�������ʱ����ƻ���ǰ���쳣״̬.
Ҳ����˵, ��Ҫ���쳣���������е����ģ�� (�������ᵼ������ģ�� ).
'''