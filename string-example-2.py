'''
在 Python1.6 和后继版本，更多的字符串操作都可以作为字符串方法来访问,
如 下例 所示, string 模块中的许多函数只是对相对应字符串方法的封装.
'''

text = "Monty Python's Flying Circus"

print "upper", "=>", text.upper()
print "lower", "=>", text.lower()
print "split", "=>", text.split()
print "join", "=>", "+".join(text.split())
print "replace", "=>", text.replace("Python", "Perl")
print "find", "=>", text.find("Python"), text.find("Perl")
print "count", "=>", text.count("n")