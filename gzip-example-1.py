'''
gzip 模块用来读写 gzip 格式的压缩文件, 如 下例 所示.
'''

import gzip

file = gzip.GzipFile("samples/sample.gz")

print file.read()