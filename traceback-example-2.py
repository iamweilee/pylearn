'''
下例 使用 StringIO 模块将跟踪返回信息放在字符串中.
'''

import traceback
import StringIO

try:
    raise IOError, "an i/o error occurred"
except:
    fp = StringIO.StringIO()
    traceback.print_exc(file=fp)
    message = fp.getvalue()
    
    print "failure! the error was:", repr(message)