'''
���� �еĽű�������һ�� keyboard ����.
���������ڳ������ֶ����ƽ���������.
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
�����氡, ��func�����ж���ı��� a=10 ��Ȼ�����ڿ���̨��ӡ����, �����Ǵ���ͬһ������
'''