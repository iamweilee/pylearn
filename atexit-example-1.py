'''
atexit ģ��������ע��һ��������ֹ����(������ô��), ��Щ�������ڽ�������ֹǰ���Զ�����.
���� register ����, ����Խ�����ע��Ϊ��ֹ����, �� ���� ��ʾ.
��Ҳ������Ӹ���Ĳ���, ��Щ����Ϊ exit �����Ĳ�������.
'''

import atexit

def exit(*args):
    print "exit", args

# register two exit handler, ���ע��ĺ���������ִ��
atexit.register(exit)
atexit.register(exit, 1)
atexit.register(exit, "hello", "world")

'''
��ģ����ʵ��һ���� sys.exitfunc ����( hook )�ļ򵥷�װ.

Ϊ�����ע��Ĳ���ȴ���ȱ���������......
'''