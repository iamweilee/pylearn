'''
modules 字典包含所有已加载的模块.
import 语句在从磁盘导入内容之前会先检查这个字典.
正如你在 下例 中所见到的, Python 在处理你的脚本之前就已经导入了很多模块.
'''

import sys

print sys.modules.keys()