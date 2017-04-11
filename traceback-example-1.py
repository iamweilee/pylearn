'''
下例 展示了 traceback 模块允许你在程序里打印异常的跟踪返回(Traceback)信息, 类似未捕获异常时解释器所做的.
'''

# 注意! 导入 traceback 会清理掉异常状态, 所以
# 最好别在异常处理代码中导入该模块

import traceback

try:
    raise SyntaxError, "example"
except:
    traceback.print_exc()