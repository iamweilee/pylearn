'''
walk ����������ҳ�һ��Ŀ¼���µ������ļ� (��������ʾ).
���Ĳ���������Ŀ¼��, �ص�����, �Լ����ݸ��ص����������ݶ���.
'''

import os

def callback(arg, directory, files):
    for file in files:
        print os.path.join(directory, file), repr(arg)
        
        
os.path.walk(".", callback, "secret message")