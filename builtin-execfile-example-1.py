'''
Python ���ṩ�� execfile ����, һ�����ļ����ش���, �������, ִ�д���Ŀ�ݷ�ʽ.
���� �򵥵�չʾ�����ʹ���������.
'''

execfile("hello.py")

def EXECFILE(filename, locals=None, globals=None):
    exec compile(open(filename).read(), filename, "exec") in locals, globals
    
EXECFILE("hello.py")