'''
�����ʹ�� copy_reg ģ��ע�����Լ�����չ����.
���� pickle �� copy ģ��ͻ�֪����δ���Ǳ�׼����.
��׼�� pickle ʵ�ֲ����������� Python code ����, �� ���� ��ʾ.
'''

import pickle

CODE = """
print 'good evening'
"""

code = compile(CODE, "<string>", "exec")

exec code
exec pickle.loads(pickle.dumps(code))