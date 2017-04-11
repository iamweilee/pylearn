'''
下例 绕了些无用的弯子, 不过它很好地说明了如何使用 errorcode 字典把数字错误码映射到符号名称( symbolic name ).
'''

import errno

try:
    fp = open("no.such.file")
except IOError, (error, message):
    print error, repr(message)
    print errno.errorcode[error]