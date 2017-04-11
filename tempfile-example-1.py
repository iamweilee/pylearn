'''
下例中展示的 tempfile 模块允许你快速地创建名称唯一的临时文件供使用.
'''

import tempfile
import os

tempfile = tempfile.mktemp()
print "tempfile", "=>", tempfile

file = open(tempfile, "w+b")
file.write("*" * 1000)
file.seek(0)

print len(file.read()), "bytes"
file.close()

try:
    # must remove file when done
    os.remove(tempfile)
except OSError:
    pass