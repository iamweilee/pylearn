'''
system �����ڵ�ǰ������ִ��һ��������, ���ȴ������.
'''

import os

if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

os.system(command)

'''
����ͨ������ϵͳ�ı�׼ shell ִ��, ������ shell ���˳�״̬.
��Ҫע������� Windows 95/98 ��, shell ͨ���� command.com , �����˳�״̬���� 0.
���� os.system ֱ�ӽ�����ݸ� shell , ��������㲻��鴫�������ʱ����Σ�� (�������� os.system("viewer %s" % file) ,
�� file ��������Ϊ "sample.jpg; rm -rf $HOME" .... ).
�����ȷ�������İ�ȫ��, ��ô���ʹ�� exec �� spawn ����(�Ժ����).
'''