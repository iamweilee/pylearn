'''
getrefcount ���� (�� ���� ��ʾ) ���ظ�����������ü��� - Ҳ�����������ʹ�ô���.
Python ��������ֵ, ��������Ϊ 0 ��ʱ��, �������������.
'''

import sys

variable = 1234

print sys.getrefcount(0)
print sys.getrefcount(variable)
print sys.getrefcount(None)


'''
ע�����ֵ���Ǳ�ʵ�ʵ�������, ��Ϊ�ú���������ȷ�����ֵ��ʱ�������������.
'''