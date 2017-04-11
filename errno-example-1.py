'''
errno 模块定义了许多的符号错误码, 比如 ENOENT ("没有该目录入口") 以及EPERM ("权限被拒绝").
它还提供了一个映射到对应平台数字错误代码的字典.
下例 展示了如何使用 errno 模块.
在大多情况下, IOError 异常会提供一个二元元组, 包含对应数值错误代码和一个说明字符串.
如果你需要区分不同的错误代码, 那么最好在可能的地方使用符号名称.
'''

import errno

try:
    fp = open("no.such.file")
except IOError, (error, message): # 这里貌似会提示SyntaxError
    if error == errno.ENOENT:
        print "no such file"
    elif error == errno.EPERM:
        print "permission denied"
    else:
        print message


# 如下所示的写法不会有语法错误

try:
    fp = open("no.such.file")
except IOError, error:
    if error[0] == errno.ENOENT:
        print "no such file"
    elif error[0] == errno.EPERM:
        print "permission denied"
    else:
        print error[1]