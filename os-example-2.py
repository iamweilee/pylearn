'''
os ģ��Ҳ������һЩ����Ŀ¼����ĺ���.
listdir �������ظ���Ŀ¼�������ļ���(����Ŀ¼��)��ɵ��б�,
��������ʾ. �� Unix �� Windows ��ʹ�õĵ�ǰĿ¼�͸�Ŀ¼���(.�� .. )�������ڴ��б���.
'''

import os
for file in os.listdir("samples"):
    print file