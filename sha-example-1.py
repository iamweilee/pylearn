'''
sha ģ���ṩ�˼�����ϢժҪ(����)�����ַ���, �� ���� ��ʾ. ���� md5 ģ������, �����ɵ��� 160 λǩ��.
'''

import sha

hash = sha.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())
print hash.hexdigest()

'''
���� sha ���ĵ�ʹ��, ����� md5 �е�����.
'''