'''
base64 ������ϵ���ڽ��������������ת��Ϊ���ı�.
����һ�� 3 �ֽڵĶ������ֽ���ת��Ϊ 4 ���ı��ַ��鴢��, ���ҹ涨ֻ�������¼����е��ַ�����:

ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789+/

����, = ���������������ĩβ.
���� չʾ�����ʹ�� encode �� decode ���������ļ�����.
'''

import base64

MESSAGE = "life of brian"

file = open("out.txt", "w")
file.write(MESSAGE)
file.close()

base64.encode(open("out.txt"), open("out.b64", "w"))
base64.decode(open("out.b64"), open("out.txt", "w"))

print "original:", repr(MESSAGE)
print "encoded message:", repr(open("out.b64").read())
print "decoded message:", repr(open("out.txt").read())