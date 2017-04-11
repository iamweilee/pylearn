'''
removedirs 函数会删除所给路径中最后一个目录下所有的空目录.
而 mkdir 和 rmdir 函数只能处理单个目录级. 
'''

import os
os.mkdir("test")
os.rmdir("test")
os.rmdir("samples") # this will fail

'''
如果需要删除非空目录, 你可以使用 shutil 模块中的 rmtree 函数.
'''