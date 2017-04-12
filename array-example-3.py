'''
该模块还提供了用于转换原始二进制数据到整数序列(或浮点数数列, 具体情况决定)的方法, 如 下例 所示.
'''

import array

a = array.array("i", "fish license") # signed integer

print a
print repr(a.tostring())
print a.tolist()