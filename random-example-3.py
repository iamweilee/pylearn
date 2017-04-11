'''
在 2.0 及以后版本, shuffle 函数可以用于打乱一个列表的内容 (也就是生成一个该列表的随机全排列).
下例 展示了如何在旧版本中实现该函数.
'''

import random

try:
    # available in 2.0 and later
    shuffle = random.shuffle
except AttributeError:
    def shuffle(x):
        for i in xrange(len(x)-1, 0, -1):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = int(random.random() * (i+1))
            x[i], x[j] = x[j], x[i]
            
            
cards = range(52)
shuffle(cards)
myhand = cards[:5]
print myhand

'''
xrange 用法与 range 完全相同, 所不同的是生成的不是一个list对象, 而是一个生成器.
由上面的示例可以知道: 要生成很大的数字序列的时候, 用xrange会比range性能优很多, 因为不需要一上来就开辟一块很大的内存空间.

xrange 和 range 这两个基本上都是在循环的时候用.

for i in range(0, 100): 
    print i 

for i in xrange(0, 100): 
    print i 

这两个输出的结果都是一样的, 实际上有很多不同, range会直接生成一个list对象, 而xrange则不会直接生成一个list, 而是每次调用返回其中的一个值.
所以xrange做循环的性能比range好, 尤其是返回很大的时候.
尽量用xrange吧, 除非你是要返回一个列表.
'''