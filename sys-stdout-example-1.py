'''
stdin , stdout , 以及 stderr 变量包含与标准 I/O 流对应的流对象.
如果需要更好地控制输出,而 print 不能满足你的要求, 它们就是你所需要的.
你也可以 替换 它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们.
'''

import sys
import string

class Redirect:
    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, s):
        self.stdout.write(string.lower(s))

# redirect standard output (including the print statement)
# 重定向标准输出(包括 print 语句)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print "HEJA SVERIGE",
print "FRISKT HUM\303\226R"

# restore standard output
# 恢复标准输出
sys.stdout = old_stdout
print "M\303\205\303\205\303\205\303\205L!"


'''
要重定向输出只要创建一个对象, 并实现它的 write 方法.
(除非 C 类型的实例外： Python 使用一个叫做 softspace 的整数属性来控制输出中的空白.
如果没有这个属性, Python 将把这个属性附加到这个对象上.
你不需要在使用 Python 对象时担心, 但是在重定向到一个 C 类型时, 你应该确保该类型支持 softspace 属性.)
'''