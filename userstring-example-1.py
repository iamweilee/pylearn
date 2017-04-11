'''
(2.0 ����) UserString ģ�����������, UserString �� MutableString.
ǰ���ǶԱ�׼�ַ������͵ķ�װ, ������һ������, �������޸��ض�λ�õ��ַ�(�������б��֪����).
ע�� MutableString ������Ч�ʺܺ�, ��������ͨ����Ƭ���ַ�������ʵ�ֵ�.
������ܺܶ���Ľű���˵��Ҫ�Ļ�, �����ʹ���ַ���Ƭ�ϵ��б����array ģ��.
���� չʾ�� UserString ģ��.
'''

import UserString

class MyString(UserString.MutableString):
    def append(self, s):
        self.data = self.data + s

    def insert(self, index, s):
        self.data = self.data[:index] + s + self.data[index:]

    def remove(self, s):
        self.data = self.data.replace(s, "")


file = open("samples/book.txt")
text = file.read()
file.close()

book = MyString(text)

for bird in ["gannet", "robin", "nuthatch"]:
    book.remove(bird)

# book.insert(5, 'iguzhi')

print book