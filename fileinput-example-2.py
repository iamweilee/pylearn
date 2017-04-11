'''
��Ҳ����ʹ�� fileinput ģ���õ�ǰ�е�Ԫ��Ϣ (meta information).
���а��� isfirstline , filename , lineno , �� ���� ��ʾ.
'''

import fileinput
import glob
import string, sys

for line in fileinput.input(glob.glob("samples/sample.txt")):
    if fileinput.isfirstline(): # first in a file?
        sys.stderr.write("-- reading %s --\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))