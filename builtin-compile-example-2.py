'''
ʹ�� compile ��������﷨, �ɹ�ִ�к�, compile �����᷵��һ���������, �����ʹ�� exec ���ִ����
'''

BODY = """
print 'the ant, an introduction'
"""
code = compile(BODY,"<script>", "exec")
print code
exec code