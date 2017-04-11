'''
makedirs 和 removedirs 函数用于创建或删除目录层.
removedirs 函数会删除所给路径中最后一个目录下所有的空目录.
而 mkdir 和 rmdir 函数只能处理单个目录级.
'''

import os
os.makedirs("test/multiple/levels")
fp = open("test/multiple/levels/file", "w")
fp.write("inspector praline")
fp.close()
# remove the file
os.remove("test/multiple/levels/file")
# and all empty directories above it 
os.removedirs("test/multiple/levels")