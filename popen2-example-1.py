'''
popen2 模块允许你执行外部命令, 并通过流来分别访问它的 stdin 和 stdout( 可能还有 stderr ).
在 python 1.5.2 以及之前版本, 该模块只存在于 Unix 平台上. 2.0 后, Windows 下也实现了该函数.
下例 展示了如何使用该模块来给字符串排序.
'''

import popen2, string

fin, fout = popen2.popen2("sort")

fout.write("foo\n")
fout.write("bar\n")
fout.close()

print fin.readline(),
print fin.readline(),
fin.close()