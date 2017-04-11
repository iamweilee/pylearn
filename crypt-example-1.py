'''
(可选, 只用于 Unix) crypt 模块实现了单向的 DES 加密, Unix 系统使用这个加密算法来储存密码, 这个模块真正也就只在检查这样的密码时有用.
下例 展示了如何使用 crypt.crypt 来加密一个密码, 将密码和 salt组合起来然后传递给函数, 这里的 salt 包含两位随机字符.
现在你可以扔掉原密码而只保存加密后的字符串了.
'''

import crypt
import random, string
import pwd

def getsalt(chars = string.letters + string.digits):
    # generate a random 2-character 'salt'
    # 生成随机的 2 字符 'salt'
    return random.choice(chars) + random.choice(chars)

print crypt.crypt("bananas", getsalt())

'''
确认密码时, 只需要用新密码调用加密函数, 并取加密后字符串的前两位作为 salt 即可.
如果结果和加密后字符串匹配, 那么密码就是正确的.
下例 使用 pwd 模块来获取已知用户的加密后密码.
'''

def login(user, password):
    "Check if user would be able to log in using password"
    try:
        pw1 = pwd.getpwnam(user)[1]
        pw2 = crypt.crypt(password, pw1[:2])
        return pw1 == pw2
    except KeyError:
        return 0 # no such user
    
user = raw_input("username:")
password = raw_input("password:")

if login(user, password):
    print "welcome", user
else:
    print "login failed"
    

'''
关于其他实现验证的方法请参阅 md5 模块一节.
'''