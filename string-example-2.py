'''
�� Python1.6 �ͺ�̰汾��������ַ���������������Ϊ�ַ�������������,
�� ���� ��ʾ, string ģ���е���ຯ��ֻ�Ƕ����Ӧ�ַ��������ķ�װ.
'''

text = "Monty Python's Flying Circus"

print "upper", "=>", text.upper()
print "lower", "=>", text.lower()
print "split", "=>", text.split()
print "join", "=>", "+".join(text.split())
print "replace", "=>", text.replace("Python", "Perl")
print "find", "=>", text.find("Python"), text.find("Perl")
print "count", "=>", text.count("n")