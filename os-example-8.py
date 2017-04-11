'''
system 函数在当前进程下执行一个新命令, 并等待它完成.
'''

import os

if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

os.system(command)

'''
命令通过操作系统的标准 shell 执行, 并返回 shell 的退出状态.
需要注意的是在 Windows 95/98 下, shell 通常是 command.com , 它的退出状态总是 0.
由于 os.system 直接将命令传递给 shell , 所以如果你不检查传入参数的时候会很危险 (比如命令 os.system("viewer %s" % file) ,
将 file 变量设置为 "sample.jpg; rm -rf $HOME" .... ).
如果不确定参数的安全性, 那么最好使用 exec 或 spawn 代替(稍后介绍).
'''