'''
removedirs ������ɾ������·�������һ��Ŀ¼�����еĿ�Ŀ¼.
�� mkdir �� rmdir ����ֻ�ܴ�����Ŀ¼��. 
'''

import os
os.mkdir("test")
os.rmdir("test")
os.rmdir("samples") # this will fail

'''
�����Ҫɾ���ǿ�Ŀ¼, �����ʹ�� shutil ģ���е� rmtree ����.
'''