'''
���� ����Щ���õ�����, �������ܺõ�˵�������ʹ�� errorcode �ֵ�����ִ�����ӳ�䵽��������( symbolic name ).
'''

import errno

try:
    fp = open("no.such.file")
except IOError, (error, message):
    print error, repr(message)
    print errno.errorcode[error]