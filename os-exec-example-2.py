'''
�� Unix ������, �����ͨ�����ʹ�� exec , fork �Լ� wait �������ӵ�ǰ
���������һ������, �� ���� ��ʾ. fork �������Ƶ�ǰ����, wait
������ȴ�һ���ӽ���ִ�н���.
'''

import os
import sys

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) + args)
    return os.wait()[0]


run("python", "hello.py")
print "goodbye"


'''
fork �������ӽ��̷����з��� 0 (����������ȴ� fork ����ֵ), �ڸ������з���һ���� 0 �Ľ��̱�ʶ��(�ӽ��̵� PID ).
Ҳ����˵, ֻ�е����Ǵ����ӽ��̵�ʱ�� "not pid " ��Ϊ��.
'''