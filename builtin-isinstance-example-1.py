'''
������� operator ģ�����ҵ��������Ƿ�Ϊĳһ�ڽ�����(����, ����, �����ֵ��) �ĺ���.
����, ��Ϊ����һ����ܼ�(����ʵ�ֻ������з�������), ���Զ���Щ����ʹ����ʽ�������жϲ����Ǻ�����.
�ڴ������ʵ����ʱ��Ḵ��Щ. Python ���������Ϊ�����ϵ����ͶԴ�;
�෴��, ���е��඼����һ�������������(special class type), ���е���ʵ������һ�������ʵ������(special instance type).
����ζ���㲻��ʹ�� type ����������һ��ʵ���Ƿ�����һ����������; ���е�ʵ������ͬ��������!
Ϊ�˽���������, �����ʹ�� isinstance ����, ������һ�������ǲ��Ǹ�����(��������)��ʵ��.
��������� չʾ�� isinstance ������ʹ��.
'''

class A:
    pass
class B:
    pass
class C(A):
    pass
class D(A, B):
    pass

def dump(object):
    print object, "=>",
    if isinstance(object, A):
        print "A",
    if isinstance(object, B):
        print "B",
    if isinstance(object, C):
        print "C",
    if isinstance(object, D):
        print "D",
    print
        
a = A()
b = B()
c = C()
d = D()
dump(a)
dump(b)
dump(c)
dump(d)
dump(0)
dump("string")