'''
makedirs �� removedirs �������ڴ�����ɾ��Ŀ¼��.
removedirs ������ɾ������·�������һ��Ŀ¼�����еĿ�Ŀ¼.
�� mkdir �� rmdir ����ֻ�ܴ�����Ŀ¼��.
'''

import os
os.makedirs("test/multiple/levels")
fp = open("test/multiple/levels/file", "w")
fp.write("inspector praline")
fp.close()
# remove the file
os.remove("test/multiple/levels/file")
# and all empty directories above it 
os.removedirs("test/multiple/levels")