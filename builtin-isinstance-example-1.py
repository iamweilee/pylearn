'''
你可以在 operator 模块中找到检查对象是否为某一内建类型(数字, 序列, 或者字典等) 的函数.
但是, 因为创建一个类很简单(比如实现基本序列方法的类), 所以对这些类型使用显式的类型判断并不是好主意.
在处理类和实例的时候会复杂些. Python 不会把类作为本质上的类型对待;
相反地, 所有的类都属于一个特殊的类类型(special class type), 所有的类实例属于一个特殊的实例类型(special instance type).
这意味着你不能使用 type 函数来测试一个实例是否属于一个给定的类; 所有的实例都是同样的类型!
为了解决这个问题, 你可以使用 isinstance 函数, 它会检查一个对象是不是给定类(或其子类)的实例.
下面的例子 展示了 isinstance 函数的使用.
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