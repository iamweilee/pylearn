'''
copy ģ�������������, ������������, �� ���� ��ʾ.
copy(object) => object ������������� "ǳ/ǳ��(shallow)" ����(copy).
���� "ǳ/ǳ��(shallow)" ����˼�Ǹ��ƶ�����, ����������һ������ (container) ʱ, ���ĳ�Ա��Ȼָ��ԭ���ĳ�Ա����.
'''

import copy

a = [[1],[2],[3]]
b = copy.copy(a)

print "before", "=>"
print a
print b

# modify original
a[0][0] = 0
a[1] = None

print "after", "=>"
print a
print b


'''
��Ҳ����ʹ��[:]��� (������Ƭ) �����б����ǳ�㸴��, Ҳ����ʹ�� copy ���������ֵ�.
�෴��, deepcopy(object) => object ����һ���������㿽��(deepcopy),
�� ���� ��ʾ, ������Ϊһ������ʱ, ���еĳ�Ա�����ݹ�ظ�����.
'''

a = [[1],[2],[3]]
b = copy.deepcopy(a)

print "before", "=>"
print a
print b

# modify original
a[0][0] = 0
a[1] = None

print "after", "=>"
print a
print b