'''
��ʱ��Ԫ��ת����ʱ��ֵ�ǳ���, ��������̸�۵ĵ���ʱ�� (local time) ���.
ֻҪ��ʱ��Ԫ�鴫�ݸ� mktime ����, �� ���� ��ʾ.
'''

import time

t0 = time.time()
tm = time.localtime(t0)

print tm
print t0
print time.mktime(tm)