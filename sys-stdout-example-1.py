'''
stdin , stdout , �Լ� stderr �����������׼ I/O ����Ӧ��������.
�����Ҫ���õؿ������,�� print �����������Ҫ��, ���Ǿ���������Ҫ��.
��Ҳ���� �滻 ����, ��ʱ����Ϳ����ض�����������뵽�����豸( device ), �����ԷǱ�׼�ķ�ʽ��������.
'''

import sys
import string

class Redirect:
    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, s):
        self.stdout.write(string.lower(s))

# redirect standard output (including the print statement)
# �ض����׼���(���� print ���)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print "HEJA SVERIGE",
print "FRISKT HUM\303\226R"

# restore standard output
# �ָ���׼���
sys.stdout = old_stdout
print "M\303\205\303\205\303\205\303\205L!"


'''
Ҫ�ض������ֻҪ����һ������, ��ʵ������ write ����.
(���� C ���͵�ʵ���⣺ Python ʹ��һ������ softspace ��������������������еĿհ�.
���û���������, Python ����������Ը��ӵ����������.
�㲻��Ҫ��ʹ�� Python ����ʱ����, �������ض���һ�� C ����ʱ, ��Ӧ��ȷ��������֧�� softspace ����.)
'''