'''
cStringIO 是一个可选的模块, 是 StringIO 的更快速实现.
它的工作方式和StringIO 基本相同, 但是它不可以被继承.
下例 展示了 cStringIO的用法.
'''

import cStringIO

MESSAGE = "That man is depriving a village somewhere of a computerscientist."

file = cStringIO.StringIO(MESSAGE)
print file.read()