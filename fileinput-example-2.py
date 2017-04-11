'''
你也可以使用 fileinput 模块获得当前行的元信息 (meta information).
其中包括 isfirstline , filename , lineno , 如 下例 所示.
'''

import fileinput
import glob
import string, sys

for line in fileinput.input(glob.glob("samples/sample.txt")):
    if fileinput.isfirstline(): # first in a file?
        sys.stderr.write("-- reading %s --\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))