'''
Python 2.0 �Լ��Ժ�汾�ṩ�� sys.byteorder ����, ���Ը��򵥵��ж��ֽ��� (����ֵΪ "little " �� "big " ), �� ���� ��ʾ.
'''

import sys

# 2.0 and later
if sys.byteorder == "little":
    print "little-endian platform (intel, alpha)"
else:
    print "big-endian platform (motorola, sparc)"