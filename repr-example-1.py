'''
repr 模块提供了内建 repr 函数的另个版本.
它限制了很多(字符串长度, 递归等).
下例 展示了如何使用该模块.
'''

# note: this overrides the built-in 'repr' function
from repr import repr

# an annoyingly recursive data structure
data = (
"X" * 100000,
)

data = [data]
data.append(data)

print repr(data)