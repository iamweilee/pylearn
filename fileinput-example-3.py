'''
�ı��ļ����滻�����ܼ�. ֻ��Ҫ�� inplace �ؼ��ֲ�������Ϊ 1 , ���ݸ� input ����, ��ģ����������һ��.
���� չʾ����Щ.
'''

import fileinput, sys

for line in fileinput.input("samples/sample1.txt", inplace=1):
    # convert Windows/DOS text files to Unix files
    if line[-2:] == "\r\n":
        line = line[:-2] + "\n"
    sys.stdout.write(line)