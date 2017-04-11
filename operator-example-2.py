'''
下例 展示了一些可以用于检查对象类型的 operator 函数.
'''

import operator
import UserList

def dump(data):
    print type(data), "=>",
    if operator.isCallable(data):
        print "CALLABLE",
    if operator.isMappingType(data):
        print "MAPPING",
    if operator.isNumberType(data):
        print "NUMBER",
    if operator.isSequenceType(data):
        print "SEQUENCE",
    print
    
    
dump(0)
dump("string")
dump("string"[0])
dump([1, 2, 3])
dump((1, 2, 3))
dump({"a": 1})
dump(len) # function 函数
dump(UserList) # module 模块
dump(UserList.UserList) # class 类
dump(UserList.UserList()) # instance 实例


'''
这里需要注意 operator 模块使用非常规的方法处理对象实例.
所以使用 isNumberType , isMappingType , 以及 isSequenceType 函数的时候要小心, 这很容易降低代码的扩展性.
同样需要注意的是一个字符串序列成员 (单个字符) 也是序列.
所以当在递归函数使用 isSequenceType 来截断对象树的时候, 别把普通字符串作为参数(或者是任何包含字符串的序列对象).
'''

'''
UserDict,UserList, 以及UserString是对应内建类型的顶层简单封装. 和内建类型不同的是, 这些封装是可以被继承的. 这在你需要一个和内建类型行为相似但由额外新方法的类的时候很有用.
UserList 模块包含了一个可继承的列表类 (事实上是对内建列表类型的 Python 封装).
'''

class AutoList(UserList.UserList):
    def __setitem__(self, i, item):
        if i == len(self.data):
            self.data.append(item)
        else:
            self.data[i] = item


list = AutoList()
for i in range(10):
    list[i] = i
    
print list