'''
stat ��������������ȡһ�������ļ�����Ϣ, ��������.
������һ����Ԫ�����(stat_result ����, ���� 10 ��Ԫ��), ������ st_mode (Ȩ��ģʽ), st_ino (inode number), st_dev (device), st_nlink (number of hardlinks), st_uid (�������û� ID), st_gid (������������ ID ), st_size (��
����С, �ֽ�), st_atime (���һ�η���ʱ��), st_mtime (����޸�ʱ��),st_ctime (ƽ̨���; Unix �µ����һ��Ԫ����/metadata �޸�ʱ��, ����Windows �µĴ���ʱ��) - ������ĿҲ����Ϊ���Է���.
[!Feather ע: ԭ��Ϊ 9 ԪԪ��. ��,���ض��󲢷�Ԫ������,Ϊ struct.]
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
���ض�������Щ�����ڷ� Unix ƽ̨�����������, ���� (st_inode , st_dev )
Ϊ Unix �µ�Ϊÿ���ļ��ṩ��Ψһ��ʶ, ��������ƽ̨����Ϊ�������������� .
'''