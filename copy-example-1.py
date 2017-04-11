'''
copy 模块包含两个函数, 用来拷贝对象, 如 下例 所示.
copy(object) => object 创建给定对象的 "浅/浅层(shallow)" 拷贝(copy).
这里 "浅/浅层(shallow)" 的意思是复制对象本身, 但当对象是一个容器 (container) 时, 它的成员仍然指向原来的成员对象.
'''

import copy

a = [[1],[2],[3]]
b = copy.copy(a)

print "before", "=>"
print a
print b

# modify original
a[0][0] = 0
a[1] = None

print "after", "=>"
print a
print b


'''
你也可以使用[:]语句 (完整切片) 来对列表进行浅层复制, 也可以使用 copy 方法复制字典.
相反地, deepcopy(object) => object 创建一个对象的深层拷贝(deepcopy),
如 下例 所示, 当对象为一个容器时, 所有的成员都被递归地复制了.
'''

a = [[1],[2],[3]]
b = copy.deepcopy(a)

print "before", "=>"
print a
print b

# modify original
a[0][0] = 0
a[1] = None

print "after", "=>"
print a
print b