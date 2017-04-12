'''
下例 展示了如何将用户名和密码转换为 HTTP 基本身份验证字符串.
'''

import base64

def getbasic(user, password):
    # basic authentication (according to HTTP)
    return base64.encodestring(user + ":" + password)

print getbasic("Aladdin", "open sesame")
print base64.decodestring(getbasic("Aladdin", "open sesame"))