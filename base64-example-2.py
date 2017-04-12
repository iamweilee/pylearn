'''
下例 展示了如何使用 encodestring 和 decodestring 函数在字符串间转换.
它们是 encode 和 decode 函数的顶层封装.
使用 StringIO 对象处理输入和输出.
'''

import base64

MESSAGE = "life of brian"

data = base64.encodestring(MESSAGE)

original_data = base64.decodestring(data)

print "original:", repr(MESSAGE)
print "encoded data:", repr(data)
print "decoded data:", repr(original_data)