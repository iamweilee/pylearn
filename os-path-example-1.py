'''
os.path ģ������������ƽ̨�޹صĴ����ļ����ĺ���.
Ҳ����˵, �㲻��Ҫ����ǰ��б��, ð�ŵ�. 
'''

import os

filename = "my/little/pony.txt"
print "using", os.name, "..."
print "split", "=>", os.path.split(filename)
print "splitext", "=>", os.path.splitext(filename)
print "dirname", "=>", os.path.dirname(filename)
print "basename", "=>", os.path.basename(filename)
print "join"," =>", os.path.join(os.path.dirname(filename), os.path.basename(filename))


'''
ע������� split ֻ�ָ�����һ��(����б��).
os.path ģ���л�����ຯ��������򵥿��ٵػ�֪�ļ�����һЩ����, �� ���� ��ʾ.
'''
FILES = (
    os.curdir,
    "/",
    "file",
    "/file",
    "samples",
    "samples/sample.png",
    "directory/file",
    "../directory/file",
    "/directory/file"
)

for file in FILES:
    print file, "=>",
    if os.path.exists(file):
        print "EXISTS",
    if os.path.isabs(file):
        print "ISABS",
    if os.path.isdir(file):
        print "ISDIR",
    if os.path.isfile(file):
        print "ISFILE",
    if os.path.islink(file):
        print "ISLINK",
    if os.path.ismount(file):
        print "ISMOUNT",
    print