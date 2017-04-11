'''
你可以使用 signal 模块配置你自己的信号处理器 (signal handler), 如 下例 所示.
当解释器收到某个信号时, 信号处理器会立即执行.
'''

import signal
import time

def handler(signo, frame):
    print "got signal", signo
    
signal.signal(signal.SIGALRM, handler)

# wake me up in two seconds
signal.alarm(2)

now = time.time()

time.sleep(200)

print "slept for", time.time() - now, "seconds"

'''
貌似 signal.SIGALRM 在 windows 上不支持啊.
'''