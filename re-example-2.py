'''
下例中展示了 sub 函数, 它可以使用另个字符串替代匹配模式.
'''
import re
import string

text = "you're no fun anymore..."
# literal replace (string.replace is faster)
# 文字替换 (string.replace 速度更快)
print re.sub("fun", "entertaining", text)
# collapse all non-letter sequences to a single dash
# 将所有非字母序列转换为一个"-"(dansh,破折号)
print re.sub("[^\w]+", "-", text)
# convert all words to beeps
# 将所有单词替换为 BEEP
print re.sub("\S+", "-BEEP-", text)


'''
你也可以通过回调 (callback) 函数使用 sub 来替换指定模式. 下例展示了如何预编译模式.
'''

text = "a line of text\\012another line of text\\012etc..."

def octal(match):
    # replace octal code with corresponding ASCII character
    # 使用对应 ASCII 字符替换八进制代码
    return chr(string.atoi(match.group(1), 8))

octal_pattern = re.compile(r"\\(\d\d\d)")

print text
print octal_pattern.sub(octal, text)


'''
如果你不编译, re 模块会为你缓存一个编译后版本, 所有的小脚本中, 通常不需要编译正则表达式.
Python1.5.2 中, 缓存中可以容纳 20 个匹配模式, 而在 2.0 中, 缓存则可以容纳 100 个匹配模式.
最后, 下例中用一个模式列表匹配一个字符串. 这些模式将会组合为一个模式, 并预编译以节省时间.
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