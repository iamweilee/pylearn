'''
UserDict ģ�������һ���ɼ̳е��ֵ��� (��ʵ���Ƕ��ڽ��ֵ����͵�Python ��װ).
���� չʾ��һ����ǿ���ֵ���, ������ֵ�ʹ�� "��/+" �������ṩ�˽��ܹؼ��ֲ����Ĺ��캯��.
'''

import UserDict

class FancyDict(UserDict.UserDict):
    
    def __init__(self, data = {}, **kw):
        UserDict.UserDict.__init__(self)
        self.update(data)
        self.update(kw)

    def __add__(self, other):
        dict = FancyDict(self.data)
        dict.update(b)
        return dict


a = FancyDict(a = 1)
b = FancyDict(b = 2)

print a + b