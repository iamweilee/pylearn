'''
����㲻ȷ���ַ�����Դ�İ�ȫ��, ��ô����ʹ�� eval ��ʱ�������Щ�鷳.
����, ĳ���û����ܻ�ʹ�� __import__ �������� os ģ��, Ȼ���Ӳ��ɾ���ļ�.
'''

print eval("__import__('os').getcwd()")
#print eval("__import__('os').remove('file')")


'''
�������ǵõ���һ�� os.error �쳣, ��˵�� Python ��ʵ���ڳ���ɾ���ļ�!
���˵���, �����������׽��. ����Ը� eval �������ݵ� 2 ������, һ�������˸ñ���ʽ��ֵʱ���ƿռ���ֵ�.
���ǲ�����, ���������ݸ����ֵ�:
'''
#print eval("__import__('os').remove('file')", {})

'''
��.... ���ǻ��ǵõ��˸� os.error �쳣.
������Ϊ Python ����ֵǰ��������ֵ�, ���û�з�������Ϊ __builtins__ �ı���(������ʽ), ���ͻ�����һ��:
'''
#namespace = {}
#print eval("_ _import_ _('os').remove('file')", namespace)
#namespace.keys()


'''
������ӡ��� namespace ������, ��ᷢ����������е��ڽ�����.
[!Feather ע: ����� RP �����Ļ�, ���ӵ����__builtins__���ǵ�ǰ��__builtins__]
����ע�⵽����������������, Python �Ͳ���ȥ����Ĭ�ϵ�, ��ô���ǵĽ������Ҳ����, Ϊ���ݵ��ֵ��������һ�� __builtins__ ���.
'''
print eval("__import__('os').remove('file')", {"__builtins__": {}})


'''
��ʹ����, ����Ȼ�޷�������� CPU ���ڴ���Դ�Ĺ���. (����, ����eval("'*'*1000000*2*2*2*2*2*2*2*2*2") �������ִ�к��ʹ��ĳ���ľ�ϵͳ��Դ).
'''