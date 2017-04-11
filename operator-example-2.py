'''
���� չʾ��һЩ�������ڼ��������͵� operator ����.
'''

import operator
import UserList

def dump(data):
    print type(data), "=>",
    if operator.isCallable(data):
        print "CALLABLE",
    if operator.isMappingType(data):
        print "MAPPING",
    if operator.isNumberType(data):
        print "NUMBER",
    if operator.isSequenceType(data):
        print "SEQUENCE",
    print
    
    
dump(0)
dump("string")
dump("string"[0])
dump([1, 2, 3])
dump((1, 2, 3))
dump({"a": 1})
dump(len) # function ����
dump(UserList) # module ģ��
dump(UserList.UserList) # class ��
dump(UserList.UserList()) # instance ʵ��


'''
������Ҫע�� operator ģ��ʹ�÷ǳ���ķ����������ʵ��.
����ʹ�� isNumberType , isMappingType , �Լ� isSequenceType ������ʱ��ҪС��, ������׽��ʹ������չ��.
ͬ����Ҫע�����һ���ַ������г�Ա (�����ַ�) Ҳ������.
���Ե��ڵݹ麯��ʹ�� isSequenceType ���ض϶�������ʱ��, �����ͨ�ַ�����Ϊ����(�������κΰ����ַ��������ж���).
'''

'''
UserDict,UserList, �Լ�UserString�Ƕ�Ӧ�ڽ����͵Ķ���򵥷�װ. ���ڽ����Ͳ�ͬ����, ��Щ��װ�ǿ��Ա��̳е�. ��������Ҫһ�����ڽ�������Ϊ���Ƶ��ɶ����·��������ʱ�������.
UserList ģ�������һ���ɼ̳е��б��� (��ʵ���Ƕ��ڽ��б����͵� Python ��װ).
'''

class AutoList(UserList.UserList):
    def __setitem__(self, i, item):
        if i == len(self.data):
            self.data.append(item)
        else:
            self.data[i] = item


list = AutoList()
for i in range(10):
    list[i] = i
    
print list