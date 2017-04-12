'''
我们可以注册一个 code 对象处理器来完成目标.
处理器应包含两个部分: 一个 pickler , 接受 code 对象并返回一个只包含简单数据类型的元组, 以及一个 unpickler , 作用相反, 接受这样的元组作为参数.
如 下例 所示.
'''

import copy_reg
import pickle, marshal, types

#
# register a pickle handler for code objects
def code_unpickler(data):
    return marshal.loads(data)

def code_pickler(code):
    return code_unpickler, (marshal.dumps(code),)

copy_reg.pickle(types.CodeType, code_pickler, code_unpickler)

#
# try it out
CODE = """
print "suppose he's got a pointed stick"
"""

code = compile(CODE, "<string>", "exec")

exec code
exec pickle.loads(pickle.dumps(code))


'''
如果你是在网络中传输 pickle 后的数据, 那么请确保自定义的 unpickler 在数据接收端也是可用的.
'''