'''
���� չʾ�� StringIO ģ���ʹ��.
��ʵ����һ���������ڴ���ļ����� (�ڴ��ļ�).
�ڴ����Ҫ��׼�ļ�����ĵط�������ʹ�������滻.
'''

import StringIO

MESSAGE = "That man is depriving a village somewhere of a computerscientist."

file = StringIO.StringIO(MESSAGE)
print file.read()