'''
re ģ���ṩ��һϵ�й���ǿ���������ʽ (regular expression) ����, ������������ټ������ַ����Ƿ��������ģʽƥ�� (ʹ�� match ����),
���߰������ģʽ (ʹ�� search ����). ������ʽ���Խ���(Ҳ������)���﷨д�����ַ���ģʽ.
match ���Դ��ַ�������ʼƥ��һ��ģʽ, �� ���� ��ʾ.
���ģʽƥ����ĳЩ���� (�������ַ���, ���ģʽ����Ļ�) , ��������һ��ƥ�����.
ʹ������ group ���������ҳ�ƥ�������.
'''

import re

text = "The Attila the Hun Show"
# a single character �����ַ�
m = re.match(".", text)
if m:
    print repr("."), "=>", repr(m.group(0))
# any string of characters �κ��ַ���
m = re.match(".*", text)
if m:
    print repr(".*"), "=>", repr(m.group(0))
# a string of letters (at least one) ֻ������ĸ���ַ���(����һ��)
m = re.match("\w+", text)
if m:
    print repr("\w+"), "=>", repr(m.group(0))
# a string of digits ֻ�������ֵ��ַ���
m = re.match("\d+", text)
if m:
    print repr("\d+"), "=>", repr(m.group(0))
    
    
    
'''
����ʹ��Բ������ģʽ�б������. �ҵ�ƥ���, group �������Գ�ȡ��Щ��
������ݣ��� ���� ��ʾ. group(1) �᷵�ص�һ�������, group(2)
���صڶ��������, ����... ����㴫�ݶ�������� group ����, ���᷵��һ
��Ԫ��
'''
text ="10/15/99"
m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
if m:
    print m.group(1, 2, 3)
    
    
    
'''
search ���������ַ����ڲ���ģʽƥ��, �� ���� ��ʾ. �������п�
�ܵ��ַ�λ�ó���ƥ��ģʽ, ������߿�ʼ, һ���ҵ�ƥ��ͷ���һ��ƥ���
��. ���û���ҵ���Ӧ��ƥ��, �ͷ��� None .
'''
text = "Example 3: There is 1 date 10/25/95 in here!"

m = re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
print m.group(1), m.group(2), m.group(3)

month, day, year = m.group(1, 2, 3)
print month, day, year

date = m.group(0)
print date