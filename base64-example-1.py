'''
base64 编码体系用于将任意二进制数据转换为纯文本.
它将一个 3 字节的二进制字节组转换为 4 个文本字符组储存, 而且规定只允许以下集合中的字符出现:

ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789+/

另外, = 用于填充数据流的末尾.
下例 展示了如何使用 encode 和 decode 函数操作文件对象.
'''

import base64

MESSAGE = "life of brian"

file = open("out.txt", "w")
file.write(MESSAGE)
file.close()

base64.encode(open("out.txt"), open("out.b64", "w"))
base64.decode(open("out.b64"), open("out.txt", "w"))

print "original:", repr(MESSAGE)
print "encoded message:", repr(open("out.b64").read())
print "decoded message:", repr(open("out.txt").read())