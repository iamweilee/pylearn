'''
(2.0 新增) UserString 模块包含两个类, UserString 和 MutableString.
前者是对标准字符串类型的封装, 后者是一个变种, 允许你修改特定位置的字符(联想下列表就知道了).
注意 MutableString 并不是效率很好, 许多操作是通过切片和字符串连接实现的.
如果性能很对你的脚本来说重要的话, 你最好使用字符串片断的列表或者array 模块.
下例 展示了 UserString 模块.
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