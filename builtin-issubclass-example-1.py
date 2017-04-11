'''
issubclass 函数与此相似, 它用于检查一个类对象是否与给定类相同, 或者是给定类的子类.
注意, isinstance 可以接受任何对象作为参数, 而 issubclass 函数在接受非类对象参数时会引发 TypeError 异常.
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
    if issubclass(object, A):
        print "A",
    if issubclass(object, B):
        print "B",
    if issubclass(object, C):
        print "C",
    if issubclass(object, D):
        print "D",
    print
    
    
dump(A)
dump(B)
dump(C)
dump(D)
dump(0)
dump("string")