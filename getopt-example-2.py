'''
Ϊ���� getopt ���ҳ���ѡ��, �� ���� ��ʾ, ����һ������ѡ����б���Ϊ�� 3 ������.
���һ��ѡ�������ԵȺ�(=) ��β, ��ô��������һ�����Ӳ���.
'''

import getopt
import sys

# simulate command-line invocation
# ģ�������в���
sys.argv = ["myscript.py", "--echo", "--printer", "lp01", "message"]

opts, args = getopt.getopt(sys.argv[1:], "ep:", ["echo", "printer="])

# process options
# ����ѡ��
echo = 0
printer = None

for o, v in opts:
    if o in ("-e", "--echo"):
        echo = 1
    elif o in ("-p", "--printer"):
        printer = v
        
print "echo", "=", echo
print "printer", "=", printer
print "arguments", "=", args


'''
[!Feather ע: �Ҳ�֪���������û, �����Լ�����:
myscript.py -e -p lp01 message
myscript.py --echo --printer=lp01 message
]
'''