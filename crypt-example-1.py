'''
(��ѡ, ֻ���� Unix) crypt ģ��ʵ���˵���� DES ����, Unix ϵͳʹ����������㷨����������, ���ģ������Ҳ��ֻ�ڼ������������ʱ����.
���� չʾ�����ʹ�� crypt.crypt ������һ������, ������� salt�������Ȼ�󴫵ݸ�����, ����� salt ������λ����ַ�.
����������ӵ�ԭ�����ֻ������ܺ���ַ�����.
'''

import crypt
import random, string
import pwd

def getsalt(chars = string.letters + string.digits):
    # generate a random 2-character 'salt'
    # ��������� 2 �ַ� 'salt'
    return random.choice(chars) + random.choice(chars)

print crypt.crypt("bananas", getsalt())

'''
ȷ������ʱ, ֻ��Ҫ����������ü��ܺ���, ��ȡ���ܺ��ַ�����ǰ��λ��Ϊ salt ����.
�������ͼ��ܺ��ַ���ƥ��, ��ô���������ȷ��.
���� ʹ�� pwd ģ������ȡ��֪�û��ļ��ܺ�����.
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
��������ʵ����֤�ķ�������� md5 ģ��һ��.
'''