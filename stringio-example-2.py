'''
StringIO 类实现了内建文件对象的所有方法, 此外还有 getvalue 方法用来返回它内部的字符串值. 
'''

import StringIO

file = StringIO.StringIO()

file.write("This man is no ordinary man. ")
file.write("This is Mr. F. G. Superman.")

print file.getvalue()