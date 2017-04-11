'''
callable 函数, 可以检查一个对象是否是可调用的(无论是直接调用或是通过 apply ).
对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True.
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
注意类对象 (A 和 B) 都是可调用的; 如果调用它们, 就产生新的对象(类实例). 但是 A 类的实例不可调用, 因为它的类没有实现 __call__ 方法.
'''