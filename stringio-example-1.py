'''
下例 展示了 StringIO 模块的使用.
它实现了一个工作在内存的文件对象 (内存文件).
在大多需要标准文件对象的地方都可以使用它来替换.
'''

import StringIO

MESSAGE = "That man is depriving a village somewhere of a computerscientist."

file = StringIO.StringIO(MESSAGE)
print file.read()