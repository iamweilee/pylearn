'''
bisect 模块用于向排序后的序列插入对象.
insort(sequence, item) 将条目插入到序列中, 并且保证序列的排序.
序列可以是任意实现了 __getitem__ 和 insert 方法的序列对象.
如 下例 所示.
'''

import bisect

list = [10, 20, 30]

bisect.insort(list, 25)
bisect.insort(list, 15)

print list