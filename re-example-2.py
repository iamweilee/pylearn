'''
������չʾ�� sub ����, ������ʹ������ַ������ƥ��ģʽ.
'''
import re
import string

text = "you're no fun anymore..."
# literal replace (string.replace is faster)
# �����滻 (string.replace �ٶȸ���)
print re.sub("fun", "entertaining", text)
# collapse all non-letter sequences to a single dash
# �����з���ĸ����ת��Ϊһ��"-"(dansh,���ۺ�)
print re.sub("[^\w]+", "-", text)
# convert all words to beeps
# �����е����滻Ϊ BEEP
print re.sub("\S+", "-BEEP-", text)


'''
��Ҳ����ͨ���ص� (callback) ����ʹ�� sub ���滻ָ��ģʽ. ����չʾ�����Ԥ����ģʽ.
'''

text = "a line of text\\012another line of text\\012etc..."

def octal(match):
    # replace octal code with corresponding ASCII character
    # ʹ�ö�Ӧ ASCII �ַ��滻�˽��ƴ���
    return chr(string.atoi(match.group(1), 8))

octal_pattern = re.compile(r"\\(\d\d\d)")

print text
print octal_pattern.sub(octal, text)


'''
����㲻����, re ģ���Ϊ�㻺��һ�������汾, ���е�С�ű���, ͨ������Ҫ����������ʽ.
Python1.5.2 ��, �����п������� 20 ��ƥ��ģʽ, ���� 2.0 ��, ������������� 100 ��ƥ��ģʽ.
���, ��������һ��ģʽ�б�ƥ��һ���ַ���. ��Щģʽ�������Ϊһ��ģʽ, ��Ԥ�����Խ�ʡʱ��.
'''

def combined_pattern(patterns):
    p = re.compile(string.join(map(lambda x: "("+x+")", patterns), "|"))
    def fixup(v, m=p.match, r=range(0,len(patterns))):
        try:
            regs = m(v).regs
        except AttributeError:
            return None # no match, so m.regs will fail
        else:
            for i in r:
                if regs[i+1] != (-1, -1):
                    return i
    return fixup
#
# try it out!
patterns = [
    r"\d+",
    r"abc\d{2,4}",
    r"p\w+"
]

p = combined_pattern(patterns)

print p("129391")
print p("abc800")
print p("abc1600")
print p("python")
print p("perl")
print p("tcl")