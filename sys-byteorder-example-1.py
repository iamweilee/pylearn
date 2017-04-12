'''
Python 2.0 以及以后版本提供了 sys.byteorder 属性, 可以更简单地判断字节序 (属性值为 "little " 或 "big " ), 如 下例 所示.
'''

import sys

# 2.0 and later
if sys.byteorder == "little":
    print "little-endian platform (intel, alpha)"
else:
    print "big-endian platform (motorola, sparc)"