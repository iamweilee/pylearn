'''
repr ģ���ṩ���ڽ� repr ����������汾.
�������˺ܶ�(�ַ�������, �ݹ��).
���� չʾ�����ʹ�ø�ģ��.
'''

# note: this overrides the built-in 'repr' function
from repr import repr

# an annoyingly recursive data structure
data = (
"X" * 100000,
)

data = [data]
data.append(data)

print repr(data)