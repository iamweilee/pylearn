'''
random ģ��Ҳ�����˷Ǻ㶨�ֲ����������������.
����ʹ���� gauss (��˹)���������������˹�ֵĲ��������.
'''

import random

histogram = [0] * 20

# calculate histogram for gaussian
# noise, using average=5, stddev=1
for i in range(1000):
    i = int(random.gauss(5, 1) * 2)
    histogram[i] = histogram[i] + 1

# print the histogram
m = max(histogram)
for v in histogram:
    print "*" * (v * 50 / m)
    
    
'''
������� Python Library Reference �ҵ�������ڷǺ㶨�ֲ������������������Ϣ.

��׼�����ṩ�����������������α�����������.
��������ںܶ�Ŀ����˵�Ѿ��㹻��, ����ģ��, ��ֵ����, �Լ���Ϸ.
����ȷ�����������ʺ�����ѧ��;.
'''