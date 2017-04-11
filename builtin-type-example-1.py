'''
type 函数允许你检查一个变量的类型. 这个函数会返回一个 type descriptor (类型描述符) , 它对于 Python 解释器提供的每个类型都是不同的.
'''

def dump(value):
    print type(value), value
    
dump(1)
dump(1.0)
dump("one")