'''
walk 函数的接口多少有点晦涩 (也许只是对我个人而言, 我总是记不住参数的顺序).
下例中展示的 index 函数会返回一个文件名列表, 你可以直接使用 for-in 循环处理文件.
'''

import os

def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files

for file in index("."):
    print file