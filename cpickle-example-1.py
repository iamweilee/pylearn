'''
(可选, 注意大小写) cPickle 模块是针对 pickle 模块的一个更快的实现.
如 下例 所示.
'''

try:
    import cPickle
    pickle = cPickle
except ImportError:
    import pickle