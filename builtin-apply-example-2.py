'''
apply ������һ�������÷��ǰѹ��캯�����������ഫ�ݵ�����, �����ǹ��캯����Ҫ���ܺܶ������ʱ��.
'''
class Rectangle:
    def __init__(self, color="white", width=10, height=10):
        print "create a", color, self, "sized", width, "x", height
        
class RoundedRectangle(Rectangle):
    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,), kw)
        
        

rect = Rectangle(color="green", height= 100, width=100)
rect= RoundedRectangle(color= "blue", height = 20)


'''
Python 2.0 �ṩ����������������ͬ����. ��ֻ��Ҫʹ��һ����ͳ�ĺ������� , ʹ�� * �����Ԫ��, ** ������ֵ�.
������������ǵȼ۵�:
result = function(*args, **kwargs)
result = apply(function, args, kwargs)
'''