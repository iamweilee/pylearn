'''
下例 展示了 choice 函数, 它用来从一个序列里分拣出一个随机项目.
它可以用于列表, 元组, 以及其他序列(当然, 非空的).
'''

import random

# random choice from a list
for i in range(5):
    print random.choice([1, 2, 3, 5, 9])