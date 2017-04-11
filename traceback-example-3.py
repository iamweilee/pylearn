'''
你可以使用 extract_tb 函数格式化跟踪返回信息, 得到包含错误信息的列表, 如 下例 所示.
'''

import traceback
import sys

def function():
    raise IOError, "an i/o error occurred"

try:
    function()
except:
    info = sys.exc_info()
    for file, lineno, function, text in traceback.extract_tb(info[2]):
        print file, "line", lineno, "in", function
        print "=>", repr(text)
    print "** %s: %s" % info[:2]