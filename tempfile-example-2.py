'''
TemporaryFile �������Զ���ѡ���ʵ��ļ���, �����ļ�, �� ������ʾ.
��������ȷ�����ļ��ڹرյ�ʱ��ᱻɾ��.
(�� Unix ��, �����ɾ��һ���Ѵ򿪵��ļ�, ��ʱ�ļ��ر�ʱ���ᱻ�Զ�ɾ��. ������ƽ̨��, ��ͨ��һ������ķ�װ��ʵ��.)
'''

import tempfile

file = tempfile.TemporaryFile()

for i in range(100):
    file.write("*" * 100)
    
file.close() # removes the file!