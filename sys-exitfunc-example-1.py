'''
如果准备在退出前自己清理一些东西(比如删除临时文件), 你可以配置一个 "退出处理函数"(exit handler), 它将在程序退出的时候自动被调用.
'''

import sys

def exitfunc():
    print "world"
    
sys.exitfunc = exitfunc

print "hello"

try: # 如果不 try except 最后的print "there" 不会有任何输出; try except 后, 则会先打印最后一行的输出, 并且在之后才会调用 exitfunc 函数
    sys.exit(1)
except SystemExit:
    pass

print "there" # 如果不捕获 sys.exit(1), 这里不会被 print


'''
在 Python 2.0 以后, 你可以使用 atexit 模块来注册多个退出处理函数.
'''