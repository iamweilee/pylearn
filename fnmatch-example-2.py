'''
���� �е� translate �������Խ�һ���ļ�ƥ��ģʽת��Ϊ������ʽ.
'''

import fnmatch
import os, re

pattern = fnmatch.translate("*.png")

for file in os.listdir("samples"):
    if re.match(pattern, file):
        print file

print "(pattern was %s)" % pattern

'''
glob �� find ģ�����ڲ�ʹ�� fnmatch ģ����ʵ��.
'''