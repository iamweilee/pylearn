'''
你可以创建自己的异常类. 只需要继承内建的 Exception 类(或者它的任意一
个合适的子类)即可, 有需要时可以再重载它的 __str__ 方法.
下例展示了如何使用 exceptions 模块.
'''

# python imports this module by itself, so the following
# line isn't really needed
# python 会自动导入该模块, 所以以下这行是不必要的
# import exceptions

class HTTPError(Exception):
    # indicates an HTTP protocol error
    def __init__(self, url, errcode, errmsg):
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg
    
    def __str__(self):
        return ("<HTTPError for %s: %s %s>" % (self.url, self.errcode, self.errmsg)) 
    
    
try:
    raise HTTPError("http://www.python.org/foo", 200, "Not Found")
except HTTPError, error:
    print "url", "=>", error.url
    print "errcode", "=>", error.errcode
    print "errmsg", "=>", error.errmsg 
    raise # reraise exception