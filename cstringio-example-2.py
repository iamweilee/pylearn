'''
Ϊ������Ĵ��뾡���ܿ�, ��ͬʱ��֤���ݵͰ汾�� Python ,�����ʹ��һ��С������ cStringIO ������ʱ���� StringIO ģ��, �� ���� ��ʾ.
'''

try:
    import cStringIO
    StringIO = cStringIO
except ImportError:
    import StringIO
    
print StringIO