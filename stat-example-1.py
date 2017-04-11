'''
下例展示了 stat 模块的基本用法, 这个模块包含了一些 os.stat
函数中可用的常量和测试函数.
'''

import stat
import os, time

st = os.stat("samples/sample.txt")
print "mode", "=>", oct(stat.S_IMODE(st[stat.ST_MODE]))
print "type", "=>",
if stat.S_ISDIR(st[stat.ST_MODE]):
    print "DIRECTORY",
if stat.S_ISREG(st[stat.ST_MODE]):
    print "REGULAR",
if stat.S_ISLNK(st[stat.ST_MODE]):
    print "LINK",
print

print "size", "=>", st[stat.ST_SIZE]
print "last accessed", "=>", time.ctime(st[stat.ST_ATIME])
print "last modified", "=>", time.ctime(st[stat.ST_MTIME])
print "inode changed", "=>", time.ctime(st[stat.ST_CTIME])