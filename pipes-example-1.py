'''
(ֻ���� Unix) pipes ģ���ṩ�� "ת���ܵ� (conversion pipelines)" ��֧��.
����Դ�����������ⲿ���ߵ��õĹܵ����������ļ�.
�� ���� ��ʾ.
'''

import pipes

t = pipes.Template()

# create a pipeline
# ���� " - " ����ӱ�׼�����������
t.append("sort", "--")
t.append("uniq", "--")

# filter some text
# ������ַ��������׼���
t.copy("samples/sample.txt", "")


'''
ò�� windows �߼��汾 (windows 7��windows 8 ���ϰ汾) ֧�� commands, ��������Ϊ windows �Դ��� shell ��.
��Ϊ�����ȴ��������......
'''