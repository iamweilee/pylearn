'''
你可以使用 copy_reg 模块注册你自己的扩展类型.
这样 pickle 和 copy 模块就会知道如何处理非标准类型.
标准的 pickle 实现不能用来处理 Python code 对象, 如 下例 所示.
'''

import pickle

CODE = """
print 'good evening'
"""

code = compile(CODE, "<string>", "exec")

exec code
exec pickle.loads(pickle.dumps(code))