'''
为了增强模块对字符的处理能力, 除了字符串方法, string 模块还包含了类型
转换函数用于把字符串转换为其他类型, (如 下例 所示).
'''

import string

print int("4711"),
print string.atoi("4711"),
print string.atoi("11147", 8), # octal 八进制
print string.atoi("1267", 16), # hexadecimal 十六进制
print string.atoi("3mv", 36) # whatever...
print string.atoi("4711", 0),
print string.atoi("04711", 0),
print string.atoi("0x4711", 0)
print float("4711"),
print string.atof("1"),
print string.atof("1.23e5")


'''
大多数情况下 (特别是当你使用的是 1.6 及更高版本时) ，你可以使用 int 和float 函数代替 string 模块中对应的函数。
atoi 函数可以接受可选的第二个参数, 指定数基(number base).
如果数基为0, 那么函数将检查字符串的前几个字符来决定使用的数基: 如果为 "0x," 数基将为 16 (十六进制), 如果为 "0," 则数基为 8 (八进制). 默认数基值为 10(十进制), 当你未传递参数时就使用这个值.
在 1.6 及以后版本中, int 函数和 atoi 一样可以接受第二个参数. 与字符串版本函数不一样的是 , int 和 float 可以接受 Unicode 字符串对象.
'''