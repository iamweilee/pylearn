'''
cStringIO ��һ����ѡ��ģ��, �� StringIO �ĸ�����ʵ��.
���Ĺ�����ʽ��StringIO ������ͬ, �����������Ա��̳�.
���� չʾ�� cStringIO���÷�.
'''

import cStringIO

MESSAGE = "That man is depriving a village somewhere of a computerscientist."

file = cStringIO.StringIO(MESSAGE)
print file.read()