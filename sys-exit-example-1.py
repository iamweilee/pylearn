'''
执行至主程序的末尾时,解释器会自动退出.
但是如果需要中途退出程序, 你可以调用 sys.exit 函数, 它带有一个可选的整数参数返回给调用它的程序.
'''

import sys

print "hello"

sys.exit(1)

print "there"