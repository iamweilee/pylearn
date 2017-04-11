'''
(2.0 新增) mmap 模块提供了操作系统内存映射函数的接口, 如 下例 所示.
映射区域的行为和字符串对象类似, 但数据是直接从文件读取的.
'''

import mmap
import os

filename = "samples/sample.txt"

file = open(filename, "r+")

size = os.path.getsize(filename)
data = mmap.mmap(file.fileno(), size)

# basics
print data
print len(data), size

# use slicing to read from the file
# 使用切片操作读取文件

print repr(data[:10]), repr(data[:10])

# or use the standard file interface
# 或使用标准的文件接口, read方法会移动文件读写游标
print repr(data.read(10)), repr(data.read(10))

'''
在 Windows 下, 这个文件必须以既可读又可写的模式打开( `r+` , `w+` , 或 `a+` ), 否则 mmap 调用会失败.
[!Feather 注: 经本人测试, a+ 模式是完全可以的, 原文只有 r+ 和 w+]
'''