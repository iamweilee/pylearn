'''
shelve 模块使用数据库驱动实现了字典对象的持久保存.
shelve 对象使用字符串作为键, 但值可以是任意类型, 所有可以被 pickle 模块处理的对象都可以作为它的值.
如 下例 所示.
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