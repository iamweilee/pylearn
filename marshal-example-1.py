'''
marshal ģ����԰Ѳ������������������ - ���ַ����໥ת��, �������ǾͿ���д���ļ������������д���.
�� ���� ��ʾ.
marshal ģ��ʹ���˼򵥵���������ʽ.
����ÿ��������Ŀ, ��ʽ������ַ���������һ�����ʹ���, Ȼ����һ���������ͱ�ʶ����.
����ʹ��С�ֽ���( little-endian order )����, �ַ�������ʱ�����������ݳ�����ͬ(���ܰ������ֽ�), Ԫ����������Ķ�����ϱ�ʾ.
'''

import marshal

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
)

data = marshal.dumps(value)

# intermediate format
print type(data), len(data)

print "-"*50
print repr(data)
print "-"*50

print marshal.loads(data)