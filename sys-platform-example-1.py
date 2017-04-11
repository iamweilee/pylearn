'''
���� չʾ�� platform ����, ����������ƽ̨������.
'''

import sys
#
# emulate "import os.path" (sort of)...
if sys.platform == "win32":
    import ntpath
    pathmodule = ntpath
elif sys.platform == "mac":
    import macpath
    pathmodule = macpath
else:
    # assume it's a posix platform
    import posixpath
    pathmodule = posixpath
    
print pathmodule


'''
���͵�ƽ̨�� Windows 9X/NT(��ʾΪ win32 ), �Լ� Macintosh (��ʾΪ mac ).
���� Unix ϵͳ����, platform ͨ������ "uname -r " ��������,
���� irix6 , linux2 , ���� sunos5 (Solaris).
'''

