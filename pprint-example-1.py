'''
pprint ģ��( pretty printer )���ڴ�ӡ Python ���ݽṹ.
�������������´�ӡ�ض����ݽṹʱ��ᷢ����������(�����ʽ�Ƚ�����, �����Ķ�).
'''

import pprint
data = (
    "this is a string", [1, 2, 3, 4], ("more tuples",
    1.0, 2.3, 4.5), "this is yet another string"
)

pprint.pprint(data)