'''
eval ����ֻ��Լ򵥵ı��ʽ. ���Ҫ������Ĵ���, ��Ӧ��ʹ�� compile �� exec ����.
����ʹ�� compile ��������﷨.
'''

NAME = "script.py"
BODY = """ prnt
'owl-stretching time' """

try:
    compile(BODY, NAME, "exec")
except SyntaxError, v:
    print "syntax error:", v, "in", NAME # syntax error: invalid syntax in script.py