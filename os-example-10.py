'''
��Ҫ����һ�������ĺ�̨������΢�е㸴��, ���ȵ��� setpgrp ��������һ��"����������/process group leader".
����, ���޹ؽ����鷢�͵��ź�(ͬʱ)�������ػ����̵�����:

os.setpgrp()

Ϊ��ȷ���ػ����̴������ļ��ܹ���ó���ָ���� mode flags(Ȩ��ģʽ���?), ���ɾ�� user mode mask:

os.umask(0)

Ȼ��, ��Ӧ���ض��� stdout/stderr �ļ�, ������ֻ�Ǽ򵥵عر�����(�����ĳ�����Ҫ stdout �� stderr д�����ݵ�ʱ��, ���ܻ�������벻��������).

class NullDevice:
    def write(self, s):
        pass
sys.stdin.close()
sys.stdout = NullDevice()
sys.stderr = NullDevice()

����֮, ���� Python �� print �� C �е� printf/fprintf ���豸(device)
û�����Ӻ󲻻�ر���ĳ���, ��ʱ�ػ������е� sys.stdout.write() ����
��һ�� IOError �쳣, ����ĳ�����Ȼ�ں�̨���еĺܺ�....
����, ��ǰ�����е� _exit ��������ֹ��ǰ����. �� sys.exit ��ͬ, �����
����(caller) ������ SystemExit �쳣, ������Ȼ�����ִ��. �� ���� ��ʾ.
'''

import os
import sys
try:
    sys.exit(1)
except SystemExit, value:
    print "caught exit(%s)" % value
try:
    os._exit(2)
except SystemExit, value:
    print "caught exit(%s)" % value
    
print "bye!"