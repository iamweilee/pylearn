'''
getopt ģ��������ڳ��������ѡ��Ͳ����ĺ���, �����Դ�����ָ�ʽ��ѡ��.
�� ��ͼ ��ʾ.
���е� 2 ������ָ��������Ŀ���д��ѡ��. ѡ�������ð��(:) ��ζ�����ѡ������ж���Ĳ���.
'''

import getopt
import sys

# simulate command-line invocation
# ģ�������в���
sys.argv = ["myscript.py", "-l", "-d", "directory", "filename"]

# process options
# ����ѡ��
opts, args = getopt.getopt(sys.argv[1:], "ld:")
long = 0
directory = None

for o, v in opts:
    if o == "-l":
        long = 1
    elif o == "-d":
        directory = v

print "long", "=", long
print "directory", "=", directory
print "arguments", "=", args