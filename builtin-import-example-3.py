'''
你也可以使用这个函数（__import__）实现延迟化的模块导入 (lazy module loading). 
例如下列中的 string 模块只在第一次使用的时候导入.
'''
class LazyImport:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None
        
    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, name)
    

string = LazyImport("string")
print string.lowercase