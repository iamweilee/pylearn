'''
expanduser 函数以与大部分 Unix shell 相同的方式处理用户名快捷符号(~, 不过在 Windows 下工作不正常).
备注：经测试, 居然在windows 8 下工作正常
'''

import os
print os.path.expanduser("~/.pythonrc") # /home/effbot/.pythonrc


'''
expandvars 函数将文件名中的环境变量替换为对应值, 如 下例 所示.
'''

os.environ["USER"] = "user"
print os.path.expandvars("/home/$USER/config")
print os.path.expandvars("$USER/folders")