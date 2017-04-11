'''
code ģ���ṩ��һЩ����ģ���׼������������Ϊ�ĺ���.
compile_command ���ڽ� compile ������Ϊ����, ������ͨ����������֤�㴫�ݵ���һ����ɵ� Python ���.
�� ���� ��, ����һ��һ�еر���һ������, ������ɺ��ִ�����õ��Ĵ������ (code object).
�����������:
a = (
  1,
  2,
  3
)
print a

ע��ֻ�����ǵ���� 2 ������, Ԫ��ĸ�ֵ�����ܱ������.
'''

import code
import string


SCRIPT = [
    "a = (",
    " 1,",
    " 2,",
    " 3 ",
    ")",
    "print a"
]

script = ""

for line in SCRIPT:
    script = script + line + "\n"
    co = code.compile_command(script, "<stdin>", "exec")
    if co:
        # got a complete statement. execute it!
        print "-"*40
        print script,
        print "-"*40
        exec co
        script = ""