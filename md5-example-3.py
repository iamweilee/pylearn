'''
下例 提供了 md5 的一个变种, 你可以通过标记信息来判断它是否在网络传输过程中被修改(丢失).
'''

import md5
import array

class HMAC_MD5:
    # keyed md5 message authentication
    def __init__(self, key):
        if len(key) > 64:
            key = md5.new(key).digest()
        ipad = array.array("B", [0x36] * 64)
        opad = array.array("B", [0x5C] * 64)
        
        for i in range(len(key)):
            ipad[i] = ipad[i] ^ ord(key[i])
            opad[i] = opad[i] ^ ord(key[i])
        self.ipad = md5.md5(ipad.tostring())
        self.opad = md5.md5(opad.tostring())

    def digest(self, data):
        ipad = self.ipad.copy()
        opad = self.opad.copy()
        ipad.update(data)
        opad.update(ipad.digest())
        return opad.digest()


# simulate server end
# 模拟服务器端
key = "this should be a well-kept secret"
message = open("samples/sample.txt").read()

signature = HMAC_MD5(key).digest(message)
# (send message and signature across a public network)
# (经过由网络发送信息和签名)

# simulate client end
#模拟客户端
key = "this should be a well-kept secret"

client_signature = HMAC_MD5(key).digest(message)

if client_signature == signature:
    print "this is the original message:"
    print
    print message
else:
    print "someone has modified the message!!!"
    
    
'''
copy 方法会对这个内部对象状态做一个快照( snapshot ).
这允许你预先计算部分密文摘要(例如 上例 中的 padded key).

千万别忘记内建的伪随机生成器对于加密操作而言并不合适. 千万小心.
'''