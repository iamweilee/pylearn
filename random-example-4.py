'''
random 模块也包含了非恒定分布的随机生成器函数.
下例使用了 gauss (高斯)函数来生成满足高斯分的布随机数字.
'''

import random

histogram = [0] * 20

# calculate histogram for gaussian
# noise, using average=5, stddev=1
for i in range(1000):
    i = int(random.gauss(5, 1) * 2)
    histogram[i] = histogram[i] + 1

# print the histogram
m = max(histogram)
for v in histogram:
    print "*" * (v * 50 / m)
    
    
'''
你可以在 Python Library Reference 找到更多关于非恒定分布随机生成器函数的信息.

标准库中提供的随机数生成器都是伪随机数生成器.
不过这对于很多目的来说已经足够了, 比如模拟, 数值分析, 以及游戏.
可以确定的是它不适合密码学用途.
'''