'''
ÿ�����Ͷ���һ����Ӧ�����Ͷ���, ���������ʹ�� is ������ (�������?)���������.
'''

def load(file):
    if isinstance(file, type("")):
        file = open(file, "rb")
    return file.read()
    
print len(load("samples/sample.png")), "bytes"
print len(load(open("samples/sample.png", "rb"))), "bytes"