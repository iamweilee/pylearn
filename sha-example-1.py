'''
sha 模块提供了计算信息摘要(密文)的另种方法, 如 下例 所示. 它与 md5 模块类似, 但生成的是 160 位签名.
'''

import sha

hash = sha.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())
print hash.hexdigest()

'''
关于 sha 密文的使用, 请参阅 md5 中的例子.
'''