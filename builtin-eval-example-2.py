'''
如果你不确定字符串来源的安全性, 那么你在使用 eval 的时候会遇到些麻烦.
例如, 某个用户可能会使用 __import__ 函数加载 os 模块, 然后从硬盘删除文件.
'''

print eval("__import__('os').getcwd()")
#print eval("__import__('os').remove('file')")


'''
这里我们得到了一个 os.error 异常, 这说明 Python 事实上在尝试删除文件!
幸运地是, 这个问题很容易解决. 你可以给 eval 函数传递第 2 个参数, 一个定义了该表达式求值时名称空间的字典.
我们测试下, 给函数传递个空字典:
'''
#print eval("__import__('os').remove('file')", {})

'''
呃.... 我们还是得到了个 os.error 异常.
这是因为 Python 在求值前会检查这个字典, 如果没有发现名称为 __builtins__ 的变量(复数形式), 它就会添加一个:
'''
#namespace = {}
#print eval("_ _import_ _('os').remove('file')", namespace)
#namespace.keys()


'''
如果你打印这个 namespace 的内容, 你会发现里边有所有的内建函数.
[!Feather 注: 如果我 RP 不错的话, 添加的这个__builtins__就是当前的__builtins__]
我们注意到了如果这个变量存在, Python 就不会去添加默认的, 那么我们的解决方法也来了, 为传递的字典参数加入一个 __builtins__ 项即可.
'''
print eval("__import__('os').remove('file')", {"__builtins__": {}})


'''
即使这样, 你仍然无法避免针对 CPU 和内存资源的攻击. (比如, 形如eval("'*'*1000000*2*2*2*2*2*2*2*2*2") 的语句在执行后会使你的程序耗尽系统资源).
'''