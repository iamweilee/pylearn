'''
��һЩƽ̨��, time ģ������� strptime ����, ���������� strftime �෴.
����һ���ַ�����ģʽ, ��������Ӧ��ʱ�����, �� ���� ��ʾ.
'''

import time

# make sure we have a strptime function!
# ȷ���к��� strptime
try:
    strptime = time.strptime
except AttributeError:
    from strptime import strptime
    
print strptime("30 Nov 00", "%d %b %y")
print strptime("1 Jan 70 1:30pm", "%d %b %y %I:%M%p")

'''
ֻ����ϵͳ�� C ���ṩ����Ӧ�ĺ�����ʱ��, time.strptime �����ſ���ʹ��.
����û���ṩ��׼ʵ�ֵ�ƽ̨, strptime.py �ṩ��һ������ȫ��ʵ��.
'''