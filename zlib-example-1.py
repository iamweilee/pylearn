'''
(可选) zlib 模块为 "zlib" 压缩提供支持. (这种压缩方法是 "deflate".)
下例 展示了如何使用 compress 和 decompress 函数接受字符串参数.
'''

import zlib

MESSAGE = "life of brian"

compressed_message = zlib.compress(MESSAGE)
decompressed_message = zlib.decompress(compressed_message)

print "original:", repr(MESSAGE)
print "compressed message:", repr(compressed_message)
print "decompressed message:", repr(decompressed_message)