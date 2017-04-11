'''
stat 函数可以用来获取一个存在文件的信息, 如下例中.
它返回一个类元组对象(stat_result 对象, 包含 10 个元素), 依次是 st_mode (权限模式), st_ino (inode number), st_dev (device), st_nlink (number of hardlinks), st_uid (所有者用户 ID), st_gid (所有者所在组 ID ), st_size (文
件大小, 字节), st_atime (最近一次访问时间), st_mtime (最近修改时间),st_ctime (平台相关; Unix 下的最近一次元数据/metadata 修改时间, 或者Windows 下的创建时间) - 以上项目也可作为属性访问.
[!Feather 注: 原文为 9 元元组. 另,返回对象并非元组类型,为 struct.]
'''

import os
import time
file = "samples/sample.png"
def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print "- size:", size, "bytes"
    print "- owner:", uid, gid
    print "- created:", time.ctime(ctime)
    print "- last accessed:", time.ctime(atime)
    print "- last modified:", time.ctime(mtime)
    print "- mode:", oct(mode)
    print "- inode/dev:", ino, dev
#
# get stats for a filename
st = os.stat(file)
print "stat", file
dump(st)
print # # get stats for an open file
fp = open(file)
st = os.fstat(fp.fileno())
print "fstat", file
dump(st)


'''
返回对象中有些属性在非 Unix 平台下是无意义的, 比如 (st_inode , st_dev )
为 Unix 下的为每个文件提供了唯一标识, 但在其他平台可能为任意无意义数据 .
'''