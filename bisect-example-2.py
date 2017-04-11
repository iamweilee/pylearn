'''
bisect(sequence, item) => index 返回条目插入后的索引值, 不对序列做任何修改.
如 下例 所示.
'''

import bisect

list = [10, 20, 30]

print list
print bisect.bisect(list, 25)
print bisect.bisect(list, 15)