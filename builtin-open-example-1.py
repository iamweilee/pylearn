'''
��Ϊ Python �ڼ��ֲ����ƿռ��ģ�����ƿռ�ǰ�������ڽ�����, ����
��ʱ�������Ҫ��ʽ������ _ _builtin_ _ ģ��. ����������
�ڽ��� open ����. ��ʱ��Ҫ��ʹ��ԭ���� open ����, ����Ҫ�ű���ʽ��ָ
��ģ������.
'''

def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in("GIF87", "GIF89"):
        raise IOError, "not aGIF file"
    file.seek(0)
    return file

fp = open("samples/sample.png")
print len(fp.read()), "bytes"
fp = open("samples/sample.jpg")
print len(fp.read()), "bytes"

'''
[!Feather ע: ������� open()�����Ǹ�ʲô��ô? ���һ���ļ��Ƿ��� GIF�ļ�,
һ���������ͼƬ��ʽ�����ļ���ͷ��Ĭ�ϵĸ�ʽ.
������ļ��Ƽ�ʹ�� file()������ open() , ��Ȼ��ʱû������]
'''