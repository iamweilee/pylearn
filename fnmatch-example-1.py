'''
fnmatch ģ��ʹ��ģʽ��ƥ���ļ���.
�� ���� ��ʾ.
ģʽ�﷨�� Unix shell ����ʹ�õ���ͬ.
�Ǻ�(* ) ƥ������������ַ�, �ʺ�(? ) ƥ�䵥���ַ�. ��Ҳ����ʹ�÷�������ָ���ַ���Χ, ���� [0-9] ����һ������. ���������ַ���ƥ�����Ǳ���.
'''

import fnmatch
import os

for file in os.listdir("samples"):
    if fnmatch.fnmatch(file, "*.png"):
        print file