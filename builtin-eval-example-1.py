'''
Python 提供了在程序中与解释器交互的多种方法. 例如 eval 函数将一个字符串作为 Python 表达式求值.
你可以传递一串文本, 简单的表达式, 或者使用内建 Python 函数. 
'''

def dump(expression):
    result = eval(expression)
    print expression, "=>", result, type(result)
    
    
dump("1")
dump("1.0")
dump("'string'")
dump("1.0 + 2.0")
dump("'*' * 10")
dump("len('world')")