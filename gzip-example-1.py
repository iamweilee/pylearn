'''
gzip ģ��������д gzip ��ʽ��ѹ���ļ�, �� ���� ��ʾ.
'''

import gzip

file = gzip.GzipFile("samples/sample.gz")

print file.read()