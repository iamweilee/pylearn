'''
copytree �������ڸ�������Ŀ¼�� (�� cp -r ��ͬ), �� rmtree ��������ɾ������Ŀ¼�� (�� rm -r ).
'''

import shutil
import os

SOURCE = "samples"
BACKUP = "samples-bak"

# create a backup directory
shutil.copytree(SOURCE, BACKUP)
print os.listdir(BACKUP)

# remove it
shutil.rmtree(BACKUP)
print os.listdir(BACKUP)