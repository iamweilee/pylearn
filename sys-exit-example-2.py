'''
注意 sys.exit 并不是立即退出. 而是引发一个 SystemExit 异常.
这意味着你可以在主程序中捕获对 sys.exit 的调用.
'''

import sys

print "hello"

try:
    sys.exit(1)
except SystemExit:
    pass

print "there"