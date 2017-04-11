'''
md5 (Message-Digest Algorithm 5)ģ�����ڼ�����Ϣ����(��ϢժҪ).
md5 �㷨����һ��ǿ׳�� 128 λ����.
����ζ����������ַ����ǲ�ͬ��, ��ô�м��߿������ǵ� md5 Ҳ��ͬ.
Ҳ����˵, ����һ�� md5 ����, ��ô����û�п������ҵ�����ַ��������������ͬ.
���� չʾ�����ʹ��md5 ģ��.
'''

import md5
import string
import base64

hash = md5.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())

'''
ע�������У�����һ���������ַ���.
���� չʾ����λ��һ��ʮ�����ƻ� base64 ������ַ���.
'''

hash = md5.new()
hash.update("spam, spam, and eggs")

value = hash.digest()

print hash.hexdigest()
# �� 2.0 ǰ, ����Ӧ��д��: print string.join(map(lambda v: "%02x" % ord(v), value), "")

print base64.encodestring(value)