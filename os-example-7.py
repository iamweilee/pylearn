'''
stat 模块包含了很多可以处理该返回对象的常量及函数. 下面的代码展示了其中的一些.
可以使用 chmod 和 utime 函数修改文件的权限模式和时间属性.
'''

import os
import stat, time

infile = "samples/sample.png"
outfile = "out.png"
# copy contents
fi = open(infile, "rb")
fo = open(outfile, "wb")
while 1:
    s = fi.read(10000)
    if not s:
        break
    fo.write(s)

fi.close()
fo.close()
# copy mode and timestamp
st = os.stat(infile)
os.chmod(outfile, stat.S_IMODE(st[stat.ST_MODE]))
os.utime(outfile, (st[stat.ST_ATIME], st[stat.ST_MTIME]))

print "original", " =>"
print "mode", oct(stat.S_IMODE(st[stat.ST_MODE]))
print "atime", time.ctime(st[stat.ST_ATIME])
print "mtime", time.ctime(st[stat.ST_MTIME])
print "copy", " =>"

st= os.stat(outfile)
print "mode", oct(stat.S_IMODE(st[stat.ST_MODE]))
print "atime", time.ctime(st[stat.ST_ATIME])
print "mtime", time.ctime(st[stat.ST_MTIME])