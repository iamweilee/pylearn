'''
Python ������ʵʱ�ش������������б�. ֻҪ�����еĲ�������һ��Ԫ���У�
Ȼ��ͨ���ڽ��� apply �������ú���.
'''
def function(a, b):
    print a, b
    

apply(function, ("whither", "canada?"))
apply(function, (1, 2 + 3))

'''
Ҫ��ѹؼ��ֲ������ݸ�һ������, ����Խ�һ���ֵ���Ϊ apply �����ĵ� 3 ������
'''
apply(function, ("crunchy", "frog"))
apply(function, ("crunchy",), {"b": "frog"})
apply(function, (), {"a": "crunchy", "b": "frog"})    