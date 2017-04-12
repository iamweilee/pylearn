'''
Python �ṩ��һЩ���ڶ��������ݽ���/�����ģ��.
struct ģ�������ڶ��������ݽṹ(���� C �е� struct )�� Python Ԫ���ת��.
array ģ�齫�������������� ( C arrays )��װΪ Python ���ж���.
'''

'''
marshal �� pickle ģ�������ڲ�ͬ�� Python ����乲��/��������.
marshal ģ��ʹ���˼򵥵���������ʽ( Self-Describing Formats ), ��֧�ִ����ڽ���������, ���� code ����.
Python ����Ҳʹ���������ʽ�������������( .pyc �ļ�).
pickle ģ���ṩ�˸����ӵĸ�ʽ, ��֧���û��������, ���������ݽṹ�ȵ�.
pickle ���� Python д��, �����˵�ٶȽ���, ��������һ�� cPickle ģ��, ʹ�� C ʵ������ͬ�Ĺ���, �ٶȺ� marshal ��������.
'''

'''
һЩģ���ṩ����ǿ�ĸ�ʽ�����, ���������ڽ��� repr ������ % �ַ�����ʽ��������.
pprint ģ�鼸�����Խ��κ� Python ���ݽṹ�ܺõش�ӡ����(��߿ɶ���).
repr ģ����������滻�ڽ�ͬ������.
��ģ�����ڽ�������ͬ�����������˺ܶ������ʽ: ��ֻ������ַ�����ǰ 30 ���ַ�, ��ֻ��ӡǶ�����ݽṹ�ļ����ȼ�, �ȵ�.
'''

'''
Python ֧�ִ󲿷ֳ��������Ʊ���, ���� base64 , binhex (һ�� Macintosh ��ʽ) , quoted printable , �Լ� uu ����.
'''

'''
array ģ��ʵ����һ����Ч�����д�������. ���к��б�����, ���������е���Ŀ����Ϊ��ͬ������.
�����������д���ʱָ��.
'''

'''
���� ������һ�� array ����, Ȼ��ʹ�� tostring �������ڲ�������( internal buffer )���Ƶ��ַ���.
'''

import array

a = array.array("B", range(16)) # unsigned char
b = array.array("h", range(16)) # signed short

print a
print repr(a.tostring())

print b
print repr(b.tostring())