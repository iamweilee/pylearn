'''
expanduser ��������󲿷� Unix shell ��ͬ�ķ�ʽ�����û�����ݷ���(~, ������ Windows �¹���������).
��ע��������, ��Ȼ��windows 8 �¹�������
'''

import os
print os.path.expanduser("~/.pythonrc") # /home/effbot/.pythonrc


'''
expandvars �������ļ����еĻ��������滻Ϊ��Ӧֵ, �� ���� ��ʾ.
'''

os.environ["USER"] = "user"
print os.path.expandvars("/home/$USER/config")
print os.path.expandvars("$USER/folders")