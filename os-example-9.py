'''
Unix ϵͳ��, �����ʹ�� fork �����ѵ�ǰ����ת���̨(һ��"�ػ���/daemon").
һ����˵, ����Ҫ����(fork off)һ����ǰ���̵ĸ���, Ȼ����ֹԭ����, �� ���� ��ʾ.
'''

import os
import time

pid = os.fork()
if pid:
    os._exit(0) # kill original
    
print "daemon started"
time.sleep(10)
print "daemon terminated"