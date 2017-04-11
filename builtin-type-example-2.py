'''
每个类型都有一个对应的类型对象, 所以你可以使用 is 操作符 (对象身份?)来检查类型.
'''

def load(file):
    if isinstance(file, type("")):
        file = open(file, "rb")
    return file.read()
    
print len(load("samples/sample.png")), "bytes"
print len(load(open("samples/sample.png", "rb"))), "bytes"