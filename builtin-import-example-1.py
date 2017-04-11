'''
import ��������������ⲿģ��� (��ȻҲ����ʹ�� from-import �汾). ��������ܲ�֪��
import ��ʵ�ǿ������ڽ����� _ _import_ _ ��������.
ͨ�����Ϸ������Զ�̬�ص��ú���. ����ֻ֪��ģ������(�ַ���)��ʱ��, �⽫�ܷ���.
'''
import glob, os
modules = []
for module_file in glob.glob("*-plugin.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError:
        pass # ignore broken modules



# say hello to all modules
for module in modules:
    module.hello()