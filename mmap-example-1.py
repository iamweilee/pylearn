'''
(2.0 ����) mmap ģ���ṩ�˲���ϵͳ�ڴ�ӳ�亯���Ľӿ�, �� ���� ��ʾ.
ӳ���������Ϊ���ַ�����������, ��������ֱ�Ӵ��ļ���ȡ��.
'''

import mmap
import os

filename = "samples/sample.txt"

file = open(filename, "r+")

size = os.path.getsize(filename)
data = mmap.mmap(file.fileno(), size)

# basics
print data
print len(data), size

# use slicing to read from the file
# ʹ����Ƭ������ȡ�ļ�

print repr(data[:10]), repr(data[:10])

# or use the standard file interface
# ��ʹ�ñ�׼���ļ��ӿ�, read�������ƶ��ļ���д�α�
print repr(data.read(10)), repr(data.read(10))

'''
�� Windows ��, ����ļ������Լȿɶ��ֿ�д��ģʽ��( `r+` , `w+` , �� `a+` ), ���� mmap ���û�ʧ��.
[!Feather ע: �����˲���, a+ ģʽ����ȫ���Ե�, ԭ��ֻ�� r+ �� w+]
'''