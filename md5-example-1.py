'''
md5 (Message-Digest Algorithm 5)模块用于计算信息密文(信息摘要).
md5 算法计算一个强壮的 128 位密文.
这意味着如果两个字符串是不同的, 那么有极高可能它们的 md5 也不同.
也就是说, 给定一个 md5 密文, 那么几乎没有可能再找到另个字符串的密文与此相同.
下例 展示了如何使用md5 模块.
'''

import md5
import string
import base64

hash = md5.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())

'''
注意这里的校验和是一个二进制字符串.
下例 展示了如何获得一个十六进制或 base64 编码的字符串.
'''

hash = md5.new()
hash.update("spam, spam, and eggs")

value = hash.digest()

print hash.hexdigest()
# 在 2.0 前, 以上应该写做: print string.join(map(lambda v: "%02x" % ord(v), value), "")

print base64.encodestring(value)