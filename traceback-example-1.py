'''
���� չʾ�� traceback ģ���������ڳ������ӡ�쳣�ĸ��ٷ���(Traceback)��Ϣ, ����δ�����쳣ʱ������������.
'''

# ע��! ���� traceback ��������쳣״̬, ����
# ��ñ����쳣��������е����ģ��

import traceback

try:
    raise SyntaxError, "example"
except:
    traceback.print_exc()