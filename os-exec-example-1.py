'''
exec ������ʹ���½����滻��ǰ����(����˵��"ת������").
��������, �ַ��� "goodbye" ��Զ���ᱻ��ӡ.
'''

import os
import sys

program = "python"
arguments = ["hello.py"]

print os.execvp(program, (program,) + tuple(arguments))
print "goodbye"


'''
Python �ṩ�˺ܶ���ֲ�ͬ�� exec ����.
������ʹ�õ��� execvp ����, ����ӱ�׼·������ִ�г���, �ѵڶ�������(Ԫ��)��Ϊ�����Ĳ������ݸ�����, ��ʹ�õ�ǰ�Ļ������������г���.
�����߸�ͬ���ͺ�������� Python Library Reference .
'''