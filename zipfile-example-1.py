'''
( 2.0 新增) zipfile 模块可以用来读写 ZIP 格式.
使用 namelist 和 infolist 方法可以列出压缩档的内容, 前者返回由文件名组成的列表, 后者返回由 ZipInfo 实例组成的列表.
如 下例 所示.
'''

import zipfile

file = zipfile.ZipFile("samples/sample.zip", "r")

# list filenames
for name in file.namelist():
    print name,
print

# list file information
for info in file.infolist():
    print info.filename, info.date_time, info.file_size