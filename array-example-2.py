'''
array 对象可以作为一个普通列表对待, 如 下例 所示.
不过, 你不能连接两个不同类型的阵列.
'''

import array

a = array.array("B", [1, 2, 3])
a.append(4)

a = a + a
a = a[2:-2]

print a
print repr(a.tostring())

for i in a:
    print i,