'''
���� չʾ�����ʹ�� md5 У������������ķ�����Ӧ�����֤(�������ǽ��Ժ���������ʹ���������������������).
'''

import md5
import string, random

def getchallenge():
    # ����һ�� 16 �ֽڳ�������ַ���. ע���ڽ���α���������
    # ʹ�õ��� 24 λ������(seed), �������������ò�����..
    challenge = map(lambda i: chr(random.randint(0, 255)), range(16))
    return string.join(challenge, "")

def getresponse(password, challenge):
    # calculate combined digest for password and challenge
    # �����������ѯ(challenge)����������
    m = md5.new()
    m.update(password)
    m.update(challenge)
    return m.digest()

# server/client communication
# ������/�ͻ���ͨѶ
# 1. client connects. server issues challenge.
# 1. �ͻ�������, ������������ѯ(challenge)
print "client:", "connect"

challenge = getchallenge()

print "server:", repr(challenge)

# 2. client combines password and challenge, and calculates the response.
# 2. �ͻ��˼����������ѯ(challenge)����Ϻ������
client_response = getresponse("trustno1", challenge)

print "client:", repr(client_response)

# 3. server does the same, and compares the result with the client response. the result is a safe login in which the assword is never sent across the communication channel.
# 3. ��������ͬ������, Ȼ��ȽϽ����ͻ��˵ķ���, �ж��Ƿ������û���½. ����������û����ͨѶ�����Ĵ���.
server_response = getresponse("trustno1", challenge)

if server_response == client_response:
    print "server:", "login ok"