'''
Python 允许你实时地创建函数参数列表. 只要把所有的参数放入一个元组中，
然后通过内建的 apply 函数调用函数.
'''
def function(a, b):
    print a, b
    

apply(function, ("whither", "canada?"))
apply(function, (1, 2 + 3))

'''
要想把关键字参数传递给一个函数, 你可以将一个字典作为 apply 函数的第 3 个参数
'''
apply(function, ("crunchy", "frog"))
apply(function, ("crunchy",), {"b": "frog"})
apply(function, (), {"a": "crunchy", "b": "frog"})    