'''
ע�� sys.exit �����������˳�. ��������һ�� SystemExit �쳣.
����ζ����������������в���� sys.exit �ĵ���.
'''

import sys

print "hello"

try:
    sys.exit(1)
except SystemExit:
    pass

print "there"