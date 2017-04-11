'''
getmembers 函数返回给定类定义的所有类级别的属性和方法
getmembers 函数返回了一个有序列表. 成员在列表中名称出现的越早, 它所处的类层次就越高. 如果无所谓顺序的话, 你可以使用字典代替列表.

vars 函数与此相似, 它返回的是包含每个成员当前值的字典. 如果你使用不带参数的 vars , 它将返回当前局部名称空间的可见元素(同 locals() 函数 ).
'''
class A:
    def a(self):
        pass
    def b(self):
        pass

class B(A):
    def c(self):
        pass
    def d(self):
        pass
    
def getmembers(klass, members=None):
    # get a list of all class members, ordered by class
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members


print getmembers(A)
print getmembers(B)
print getmembers(IOError)