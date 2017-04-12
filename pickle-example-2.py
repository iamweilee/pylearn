'''
默认情况下, pickle 使用急于文本的格式.
你也可以使用二进制格式, 这样数字和二进制字符串就会以紧密的格式储存, 这样文件就会更小点.
如 下例 所示.
'''

import pickle
import math

value = (
    "this is a long string" * 100,
    [1.2345678, 2.3456789, 3.4567890] * 100
)

# text mode
data = pickle.dumps(value)

print type(data), len(data), pickle.loads(data) == value

# binary mode
data = pickle.dumps(value, 1)

print type(data), len(data), pickle.loads(data) == value