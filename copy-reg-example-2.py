'''
���ǿ���ע��һ�� code �������������Ŀ��.
������Ӧ������������: һ�� pickler , ���� code ���󲢷���һ��ֻ�������������͵�Ԫ��, �Լ�һ�� unpickler , �����෴, ����������Ԫ����Ϊ����.
�� ���� ��ʾ.
'''

import copy_reg
import pickle, marshal, types

#
# register a pickle handler for code objects
def code_unpickler(data):
    return marshal.loads(data)

def code_pickler(code):
    return code_unpickler, (marshal.dumps(code),)

copy_reg.pickle(types.CodeType, code_pickler, code_unpickler)

#
# try it out
CODE = """
print "suppose he's got a pointed stick"
"""

code = compile(CODE, "<string>", "exec")

exec code
exec pickle.loads(pickle.dumps(code))


'''
��������������д��� pickle �������, ��ô��ȷ���Զ���� unpickler �����ݽ��ն�Ҳ�ǿ��õ�.
'''