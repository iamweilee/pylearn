'''
如果你不想列出所有的文件 (基于性能或者是内存的考虑) , 下例展示了另一种方法.
这里 DirectoryWalker 类的行为与序列对象相似, 一次返回一个文件. (generator?)
'''

import os

class DirectoryWalker:
    # a forward iterator that traverses a directory tree
    def __init__(self, directory):
        self.stack = [directory]
        self.files = []
        self.index = 0

    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                return fullname


for file in DirectoryWalker("."):
    print file
    
    
'''
注意 DirectoryWalker 类并不检查传递给 __getitem__ 方法的索引值.
这意味着如果你越界访问序列成员(索引数字过大)的话, 这个类将不能正常工作.
'''