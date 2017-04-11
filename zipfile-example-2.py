'''
调用 read 方法就可以从 ZIP 文档中读取数据.
它接受一个文件名作为参数, 返回字符串.
如 下例 所示.
'''

import zipfile

file = zipfile.ZipFile("samples/sample.zip", "r")

for name in file.namelist():
    data = file.read(name)
    print name, len(data), repr(data[:10])