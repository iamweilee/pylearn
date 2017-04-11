'''
re 模块提供了一系列功能强大的正则表达式 (regular expression) 工具, 它们允许你快速检查给定字符串是否与给定的模式匹配 (使用 match 函数),
或者包含这个模式 (使用 search 函数). 正则表达式是以紧凑(也很神秘)的语法写出的字符串模式.
match 尝试从字符串的起始匹配一个模式, 如 下例 所示.
如果模式匹配了某些内容 (包括空字符串, 如果模式允许的话) , 它将返回一个匹配对象.
使用它的 group 方法可以找出匹配的内容.
'''

import re

text = "The Attila the Hun Show"
# a single character 单个字符
m = re.match(".", text)
if m:
    print repr("."), "=>", repr(m.group(0))
# any string of characters 任何字符串
m = re.match(".*", text)
if m:
    print repr(".*"), "=>", repr(m.group(0))
# a string of letters (at least one) 只包含字母的字符串(至少一个)
m = re.match("\w+", text)
if m:
    print repr("\w+"), "=>", repr(m.group(0))
# a string of digits 只包含数字的字符串
m = re.match("\d+", text)
if m:
    print repr("\d+"), "=>", repr(m.group(0))
    
    
    
'''
可以使用圆括号在模式中标记区域. 找到匹配后, group 方法可以抽取这些区
域的内容，如 下例 所示. group(1) 会返回第一组的内容, group(2)
返回第二组的内容, 这样... 如果你传递多个组数给 group 函数, 它会返回一
个元组
'''
text ="10/15/99"
m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
if m:
    print m.group(1, 2, 3)
    
    
    
'''
search 函数会在字符串内查找模式匹配, 如 下例 所示. 它在所有可
能的字符位置尝试匹配模式, 从最左边开始, 一旦找到匹配就返回一个匹配对
象. 如果没有找到相应的匹配, 就返回 None .
'''
text = "Example 3: There is 1 date 10/25/95 in here!"

m = re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
print m.group(1), m.group(2), m.group(3)

month, day, year = m.group(1, 2, 3)
print month, day, year

date = m.group(0)
print date