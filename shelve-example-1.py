'''
shelve ģ��ʹ�����ݿ�����ʵ�����ֵ����ĳ־ñ���.
shelve ����ʹ���ַ�����Ϊ��, ��ֵ��������������, ���п��Ա� pickle ģ�鴦��Ķ��󶼿�����Ϊ����ֵ.
�� ���� ��ʾ.
'''

import shelve

db = shelve.open("database", "c")
db["one"] = 1
db["two"] = 2
db["three"] = 3
db.close()

db = shelve.open("database", "r")

for key in db.keys():
    print repr(key), repr(db[key])