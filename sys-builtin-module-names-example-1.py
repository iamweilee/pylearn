'''
builtin_module_names 列表包含 Python 解释器中所有内建模块的名称.
'''

import sys

def dump(module):
    print module, "=>",
    if module in sys.builtin_module_names:
        print "<BUILTIN>"
    else:
        module = __import__(module)
        print module.__file__
        
        
dump("os")
dump("sys")
dump("string")
dump("strop")
dump("zlib")