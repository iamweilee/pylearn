'''
pickle 模块同 marshal 模块相同, 将数据连续化, 便于保存传输.
它比 marshal 要慢一些, 但它可以处理类实例, 共享的元素, 以及递归数据结构等.
'''

import pickle

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
)

data = pickle.dumps(value)

# intermediate format
print type(data), len(data)

print "-"*50
print data
print "-"*50

print pickle.loads(data)


'''
不过另一方面, pickle 不能处理 code 对象(可以参阅 copy_reg 模块来完成这个).
'''