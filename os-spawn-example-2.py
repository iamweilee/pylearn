'''
spawn �������������ں�̨����һ������. ������ �� run ���������һ����ѡ�� mode ����;
������Ϊ os.P_NOWAIT ʱ, ����ű�����ȴ��ӳ������, Ĭ��ֵ os.P_WAIT ʱ spawn ��ȴ��ӽ��̽���.
�����ı�־�������� os.P_OVERLAY ,��ʹ�� spawn ����Ϊ�� exec ����, �Լ� os.P_DETACH , ���ں�̨�����ӽ���, �뵱ǰ����̨�ͼ��̽������.
'''

import os
import string

def run(program, *args, **kw):
    # find executable
    mode = kw.get("mode", os.P_WAIT)
    for path in string.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(mode, file, (file,) + args)
        except os.error:
            pass
        raise os.error, "cannot find executable"
    

run("python", "hello.py", mode=os.P_NOWAIT)
print "goodbye"