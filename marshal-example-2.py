'''
marshal 模块还可以处理 code 对象(它用于储存预编译的 Python 模块).
如 下例 所示.
'''

import marshal

script = """
print 'hello'
"""

code = compile(script, "<script>", "exec")

data = marshal.dumps(code)

# intermediate format
print type(data), len(data)

print "-"*50
print repr(data)
print "-"*50

exec marshal.loads(data)