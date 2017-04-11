'''
下例 中的脚本定义了一个 keyboard 函数.
它允许你在程序中手动控制交互解释器.
'''

def keyboard(banner=None):
    import code, sys
    
    # use exception trick to pick up the current frame
    try:
        raise None
    except:
        frame = sys.exc_info()[2].tb_frame.f_back
        
    # evaluate commands in current namespace
    namespace = frame.f_globals.copy()
    namespace.update(frame.f_locals)
    
    code.interact(banner=banner, local=namespace)

def func():
    print "START"
    a = 10
    keyboard()
    print "END"
    
    
func()


'''
很神奇啊, 在func函数中定义的变量 a=10 居然可以在控制台打印出来, 它们是处于同一作用域啊
'''