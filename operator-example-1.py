'''
operator 模块为 Python 提供了一个 "功能性" 的标准操作符接口.
当使用map 以及 filter 一类的函数的时候, operator 模块中的函数可以替换一些lambda 函式. 而且这些函数在一些喜欢写晦涩代码的程序员中很流行.
下例 展示了 operator 模块的一般用法.
'''

import operator

sequence = 1, 2, 4
print "add", "=>", reduce(operator.add, sequence)
print "sub", "=>", reduce(operator.sub, sequence)
print "mul", "=>", reduce(operator.mul, sequence)
print "concat", "=>", operator.concat("spam", "egg")
print "repeat", "=>", operator.repeat("spam", 5)
print "getitem", "=>", operator.getitem(sequence, 2)
print "indexOf", "=>", operator.indexOf(sequence, 2)
print "sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 3)