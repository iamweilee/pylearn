'''
(ֻ���� Unix) commands ģ�����һЩ����ִ���ⲿ����ĺ���.
���� չʾ�����ģ��.
'''

import commands

stat, output = commands.getstatusoutput("ls -lR")

print "status", "=>", stat
print "output", "=>", len(output), "bytes"

'''
ò�� windows �߼��汾 (windows 7��windows 8 ���ϰ汾) ֧�� commands, ��������Ϊ windows �Դ��� shell ��.
'''