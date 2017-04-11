'''
fileinput 模块允许你循环一个或多个文本文件的内容, 如 下例 所示
'''

import fileinput
import sys

for line in fileinput.input("samples/sample.txt"):
    sys.stdout.write("-> ")
    sys.stdout.write(line)