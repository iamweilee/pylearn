'''
bisect ģ�����������������в������.
insort(sequence, item) ����Ŀ���뵽������, ���ұ�֤���е�����.
���п���������ʵ���� __getitem__ �� insert ���������ж���.
�� ���� ��ʾ.
'''

import bisect

list = [10, 20, 30]

bisect.insort(list, 25)
bisect.insort(list, 15)

print list