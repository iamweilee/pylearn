'''
errno ģ�鶨�������ķ��Ŵ�����, ���� ENOENT ("û�и�Ŀ¼���") �Լ�EPERM ("Ȩ�ޱ��ܾ�").
�����ṩ��һ��ӳ�䵽��Ӧƽ̨���ִ��������ֵ�.
���� չʾ�����ʹ�� errno ģ��.
�ڴ�������, IOError �쳣���ṩһ����ԪԪ��, ������Ӧ��ֵ��������һ��˵���ַ���.
�������Ҫ���ֲ�ͬ�Ĵ������, ��ô����ڿ��ܵĵط�ʹ�÷�������.
'''

import errno

try:
    fp = open("no.such.file")
except IOError, (error, message): # ����ò�ƻ���ʾSyntaxError
    if error == errno.ENOENT:
        print "no such file"
    elif error == errno.EPERM:
        print "permission denied"
    else:
        print message


# ������ʾ��д���������﷨����

try:
    fp = open("no.such.file")
except IOError, error:
    if error[0] == errno.ENOENT:
        print "no such file"
    elif error[0] == errno.EPERM:
        print "permission denied"
    else:
        print error[1]