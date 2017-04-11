'''
InteractiveConsole 类实现了一个交互控制台, 类似你启动的 Python 解释器交互模式.
控制台可以是活动的(自动调用函数到达下一行) 或是被动的(当有新数据时调用 push 方法).
默认使用内建的 raw_input 函数. 如果你想使用另个输入函数, 你可以使用相同的名称重载这个方法.
下例 展示了如何使用 code 模块来模拟交互解释器.
'''

import code


console = code.InteractiveConsole()
console.interact()