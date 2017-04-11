'''
(只用于 Unix) commands 模块包含一些用于执行外部命令的函数.
下例 展示了这个模块.
'''

import commands

stat, output = commands.getstatusoutput("ls -lR")

print "status", "=>", stat
print "output", "=>", len(output), "bytes"

'''
貌似 windows 高级版本 (windows 7、windows 8 以上版本) 支持 commands, 可能是因为 windows 自带了 shell 吧.
'''