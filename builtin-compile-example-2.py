'''
使用 compile 函数检查语法, 成功执行后, compile 函数会返回一个代码对象, 你可以使用 exec 语句执行它
'''

BODY = """
print 'the ant, an introduction'
"""
code = compile(BODY,"<script>", "exec")
print code
exec code