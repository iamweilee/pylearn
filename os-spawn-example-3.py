'''
下例中提供了一个在 Unix 和 Windows 平台上通用的 spawn 方法.
'''

import os
import string

if os.name in ("nt", "dos"):
    exefile = ".exe"
else:
    exefile = ""
    
def spawn(program, *args):
    try:
        # possible 2.0 shortcut!
        return os.spawnvp(program, (program,) + args)
    except AttributeError:
        pass
    try:
        spawnv = os.spawnv
    except AttributeError: # assume it's unix
        pid = os.fork()
        
        if not pid:
            os.execvp(program, (program,)+ args)
        return os.wait()[0]
    else: # got spawnv but no spawnp: go look for an executable
        for path in string.split(os.environ["PATH"], os.pathsep):
            file = os.path.join(path, program) + exefile
            try:
                return spawnv(os.P_WAIT, file, (file,) + args)
            except os.error:
                pass
            raise IOError, "cannot find executable" # # try it out!
            
            
spawn("python", "hello.py")
print "goodbye"


'''
上例中首先尝试调用 spawnvp 函数. 如果该函数不存在 (一些版本/平台没有这个函数), 它将继续查找一个名为 spawnv 的函数并且开始查找程序路
径. 作为最后的选择, 它会调用 exec 和 fork 函数完成工作.
'''