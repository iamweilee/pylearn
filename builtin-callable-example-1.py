'''
callable ����, ���Լ��һ�������Ƿ��ǿɵ��õ�(������ֱ�ӵ��û���ͨ�� apply ).
���ں���, ����, lambda ��ʽ, ��, �Լ�ʵ���� __call__ ��������ʵ��, �������� True.
'''

def dump(function):
    if callable(function):
        print function, "is callable"
    else:
        print function, "is *not* callable"
        
class A:
    def method(self, value):
        return value
    
class B(A):
    def __call__(self, value):
        return value
    

a = A()
b = B()
dump(0) # simple objects
dump("string")
dump(callable)
dump(dump) # function
dump(A) # classes
dump(B)
dump(B.method)
dump(a) # instances
dump(b)
dump(b.method)

'''
ע������� (A �� B) ���ǿɵ��õ�; �����������, �Ͳ����µĶ���(��ʵ��). ���� A ���ʵ�����ɵ���, ��Ϊ������û��ʵ�� __call__ ����.
'''