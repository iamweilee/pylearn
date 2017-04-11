'''
code 模块提供了一些用于模拟标准交互解释器行为的函数.
compile_command 与内建 compile 函数行为相似, 但它会通过测试来保证你传递的是一个完成的 Python 语句.
在 下例 中, 我们一行一行地编译一个程序, 编译完成后会执行所得到的代码对象 (code object).
程序代码如下:
a = (
  1,
  2,
  3
)
print a

注意只有我们到达第 2 个括号, 元组的赋值操作能编译完成.
'''

import code
import string


SCRIPT = [
    "a = (",
    " 1,",
    " 2,",
    " 3 ",
    ")",
    "print a"
]

script = ""

for line in SCRIPT:
    script = script + line + "\n"
    co = code.compile_command(script, "<stdin>", "exec")
    if co:
        # got a complete statement. execute it!
        print "-"*40
        print script,
        print "-"*40
        exec co
        script = ""