'''
eval 函数只针对简单的表达式. 如果要处理大块的代码, 你应该使用 compile 和 exec 函数.
下例使用 compile 函数检查语法.
'''

NAME = "script.py"
BODY = """ prnt
'owl-stretching time' """

try:
    compile(BODY, NAME, "exec")
except SyntaxError, v:
    print "syntax error:", v, "in", NAME # syntax error: invalid syntax in script.py