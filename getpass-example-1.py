'''
getpass ģ���ṩ��ƽ̨�޹ص�������������������ķ���.
�� ���� ��ʾ.
getpass(prompt) ����ʾ��ʾ�ַ���, �رռ��̵���Ļ����, Ȼ���ȡ����.
�����ʾ����ʡ��, ��ô������ӡ�� "Password: ".
getuser() ��õ�ǰ�û���, ������ܵĻ�.
'''

import getpass

usr = getpass.getuser()
pwd = getpass.getpass("enter password for user %s: " % usr)
print usr, pwd