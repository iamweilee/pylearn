'''
如果你需要处理文件大小和时间戳, 下例 给出了一个类, 它返回文件名和它的 os.stat 属性(一个元组).
这个版本在每个文件上都能节省一次或两次 stat 调用( os.path.isdir 和 os.path.islink 内部都使用了 stat ), 并且在一些平台上运行很快.
'''

import os, stat
class DirectoryStatWalker:
    # a forward iterator that traverses a directory tree, and
    # returns the filename and additional file information
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
                st = os.stat(fullname)
                mode = st[stat.ST_MODE]
                if stat.S_ISDIR(mode) and not stat.S_ISLNK(mode):
                    self.stack.append(fullname)
                return fullname, st


for file, st in DirectoryStatWalker("."):
    print file, st[stat.ST_SIZE]