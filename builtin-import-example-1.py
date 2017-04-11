'''
import 语句是用来导入外部模块的 (当然也可以使用 from-import 版本). 不过你可能不知道
import 其实是靠调用内建函数 _ _import_ _ 来工作的.
通过这个戏法你可以动态地调用函数. 当你只知道模块名称(字符串)的时候, 这将很方便.
'''
import glob, os
modules = []
for module_file in glob.glob("*-plugin.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError:
        pass # ignore broken modules



# say hello to all modules
for module in modules:
    module.hello()