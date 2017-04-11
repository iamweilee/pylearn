'''
vars 函数返回的是包含每个成员当前值的字典. 
如果你使用不带参数的 vars , 它将返回当前局部名称空间的可见元素(同 locals() 函数 ).
'''

book = "library2"
pages = 250
scripts = 350

print "the %(book)s book contains more than %(scripts)s scripts" % vars()