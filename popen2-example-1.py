'''
popen2 ģ��������ִ���ⲿ����, ��ͨ�������ֱ�������� stdin �� stdout( ���ܻ��� stderr ).
�� python 1.5.2 �Լ�֮ǰ�汾, ��ģ��ֻ������ Unix ƽ̨��. 2.0 ��, Windows ��Ҳʵ���˸ú���.
���� չʾ�����ʹ�ø�ģ�������ַ�������.
'''

import popen2, string

fin, fout = popen2.popen2("sort")

fout.write("foo\n")
fout.write("bar\n")
fout.close()

print fin.readline(),
print fin.readline(),
fin.close()