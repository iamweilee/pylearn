'''
pickle ģ��ͬ marshal ģ����ͬ, ������������, ���ڱ��洫��.
���� marshal Ҫ��һЩ, �������Դ�����ʵ��, �����Ԫ��, �Լ��ݹ����ݽṹ��.
'''

import pickle

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
)

data = pickle.dumps(value)

# intermediate format
print type(data), len(data)

print "-"*50
print data
print "-"*50

print pickle.loads(data)


'''
������һ����, pickle ���ܴ��� code ����(���Բ��� copy_reg ģ����������).
'''