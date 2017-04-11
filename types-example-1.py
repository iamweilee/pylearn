'''
types 模块包含了标准解释器定义的所有类型的类型对象, 如 下例 所示.
同一类型的所有对象共享一个类型对象. 你可以使用 is 来检查一个对象是不是属于某个给定类型.
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
注意所有的类都具有相同的类型, 所有的实例也是一样.
要测试一个类或者实例所属的类, 可以使用内建的 issubclass 和 isinstance 函数.
types 模块在第一次引入的时候会破坏当前的异常状态.
也就是说, 不要在异常处理语句块中导入该模块 (或其他会导入它的模块 ).
'''