'''
为了让 getopt 查找长的选项, 如 下例 所示, 传递一个描述选项的列表做为第 3 个参数.
如果一个选项名称以等号(=) 结尾, 那么它必须有一个附加参数.
'''

import getopt
import sys

# simulate command-line invocation
# 模仿命令行参数
sys.argv = ["myscript.py", "--echo", "--printer", "lp01", "message"]

opts, args = getopt.getopt(sys.argv[1:], "ep:", ["echo", "printer="])

# process options
# 处理选项
echo = 0
printer = None

for o, v in opts:
    if o in ("-e", "--echo"):
        echo = 1
    elif o in ("-p", "--printer"):
        printer = v
        
print "echo", "=", echo
print "printer", "=", printer
print "arguments", "=", args


'''
[!Feather 注: 我不知道大家明白没, 可以自己试下:
myscript.py -e -p lp01 message
myscript.py --echo --printer=lp01 message
]
'''