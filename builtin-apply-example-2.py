'''
apply 函数的一个常见用法是把构造函数参数从子类传递到基类, 尤其是构造函数需要接受很多参数的时候.
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
Python 2.0 提供了另个方法来做相同的事. 你只需要使用一个传统的函数调用 , 使用 * 来标记元组, ** 来标记字典.
下面两个语句是等价的:
result = function(*args, **kwargs)
result = apply(function, args, kwargs)
'''