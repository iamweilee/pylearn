'''
���� չʾ�����ʹ�� encodestring �� decodestring �������ַ�����ת��.
������ encode �� decode �����Ķ����װ.
ʹ�� StringIO ��������������.
'''

import base64

MESSAGE = "life of brian"

data = base64.encodestring(MESSAGE)

original_data = base64.decodestring(data)

print "original:", repr(MESSAGE)
print "encoded data:", repr(data)
print "decoded data:", repr(original_data)