'''
Ϊ����ǿģ����ַ��Ĵ�������, �����ַ�������, string ģ�黹����������
ת���������ڰ��ַ���ת��Ϊ��������, (�� ���� ��ʾ).
'''

import string

print int("4711"),
print string.atoi("4711"),
print string.atoi("11147", 8), # octal �˽���
print string.atoi("1267", 16), # hexadecimal ʮ������
print string.atoi("3mv", 36) # whatever...
print string.atoi("4711", 0),
print string.atoi("04711", 0),
print string.atoi("0x4711", 0)
print float("4711"),
print string.atof("1"),
print string.atof("1.23e5")


'''
���������� (�ر��ǵ���ʹ�õ��� 1.6 �����߰汾ʱ) �������ʹ�� int ��float �������� string ģ���ж�Ӧ�ĺ�����
atoi �������Խ��ܿ�ѡ�ĵڶ�������, ָ������(number base).
�������Ϊ0, ��ô����������ַ�����ǰ�����ַ�������ʹ�õ�����: ���Ϊ "0x," ������Ϊ 16 (ʮ������), ���Ϊ "0," ������Ϊ 8 (�˽���). Ĭ������ֵΪ 10(ʮ����), ����δ���ݲ���ʱ��ʹ�����ֵ.
�� 1.6 ���Ժ�汾��, int ������ atoi һ�����Խ��ܵڶ�������. ���ַ����汾������һ������ , int �� float ���Խ��� Unicode �ַ�������.
'''