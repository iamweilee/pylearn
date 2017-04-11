'''
time ģ����Լ��� Python �����ִ��ʱ��, �� ���� ��ʾ.
����Բ��� "wall time" (real world time), ����"����ʱ��" (���ĵ� CPU ʱ��).
'''

import time

def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"

'''
���������е�ϵͳ���ܲ�����ʵ�Ľ���ʱ��. һЩϵͳ��(���� Windows ), clock ����ͨ�������ӳ�������������ʱ�� wall time.
����ʱ��ľ���������. ��һЩϵͳ��, ������ 30 ���Ӻ���̻ᱻ����.
(ԭ��: On many systems, it wraps around after just over 30 minutes.)
��μ� timing ģ��( Windows �µ����Ѳ���æ����,û�е�~), �����Բ��������¼�֮��� wall time.
'''