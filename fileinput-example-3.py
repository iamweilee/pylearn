'''
文本文件的替换操作很简单. 只需要把 inplace 关键字参数设置为 1 , 传递给 input 函数, 该模块会帮你做好一切.
下例 展示了这些.
'''

import fileinput, sys

for line in fileinput.input("samples/sample1.txt", inplace=1):
    # convert Windows/DOS text files to Unix files
    if line[-2:] == "\r\n":
        line = line[:-2] + "\n"
    sys.stdout.write(line)