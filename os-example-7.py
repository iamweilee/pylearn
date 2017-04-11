'''
stat ģ������˺ܶ���Դ����÷��ض���ĳ���������. ����Ĵ���չʾ�����е�һЩ.
����ʹ�� chmod �� utime �����޸��ļ���Ȩ��ģʽ��ʱ������.
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