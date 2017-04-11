'''
为了让你的代码尽可能快, 但同时保证兼容低版本的 Python ,你可以使用一个小技巧在 cStringIO 不可用时启用 StringIO 模块, 如 下例 所示.
'''

try:
    import cStringIO
    StringIO = cStringIO
except ImportError:
    import StringIO
    
print StringIO