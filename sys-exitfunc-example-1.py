'''
���׼�����˳�ǰ�Լ�����һЩ����(����ɾ����ʱ�ļ�), ���������һ�� "�˳�������"(exit handler), �����ڳ����˳���ʱ���Զ�������.
'''

import sys

def exitfunc():
    print "world"
    
sys.exitfunc = exitfunc

print "hello"

try: # ����� try except ����print "there" �������κ����; try except ��, ����ȴ�ӡ���һ�е����, ������֮��Ż���� exitfunc ����
    sys.exit(1)
except SystemExit:
    pass

print "there" # ��������� sys.exit(1), ���ﲻ�ᱻ print


'''
�� Python 2.0 �Ժ�, �����ʹ�� atexit ģ����ע�����˳�������.
'''