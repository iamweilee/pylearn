'''
time ģ���ṩ��һЩ�������ں�һ����ʱ��ĺ���. ���ǽ����� C ����ʱ��ļ򵥷�װ.
���������ں�ʱ����Ա���ʾΪ������(�Ӳο�ʱ��, ͨ���� 1970.1.1 �����ھ���������. �� Unix ��ʽ), ����һ����ʾʱ��� struct (��Ԫ��).
����չʾ�����ʹ�� time ģ���ȡ��ǰʱ��.
'''

import time

now = time.time()

print now, "seconds since", time.gmtime(0)[:6]
print
print "or in other words:"
print "- local time:", time.localtime(now)
print "- utc:", time.gmtime(now)

'''
localtime �� gmtime ���ص���Ԫ�������, ��, ��, ʱ, ��, ��, ����, һ��ĵڼ���, �չ��־.
��������һ����λ��(����ǧ��������ƽ̨�����й涨, ��������λ��), ���ڴ�����һ(���� 0 ����)��ʼ, 1 �� 1 ����һ��ĵ�һ��.
'''