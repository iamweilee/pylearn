'''
shutil ʵ��ģ�������һЩ���ڸ����ļ����ļ��еĺ���.
���� ��ʹ�õ� copy ����ʹ�ú� Unix �� cp ���������ͬ�ķ�ʽ����һ���ļ�.
'''

import shutil
import os

for file in os.listdir("."):
    if os.path.splitext(file)[1] == ".py":
        print file
        shutil.copy(file, os.path.join("backup", file))