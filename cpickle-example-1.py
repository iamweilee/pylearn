'''
(��ѡ, ע���Сд) cPickle ģ������� pickle ģ���һ�������ʵ��.
�� ���� ��ʾ.
'''

try:
    import cPickle
    pickle = cPickle
except ImportError:
    import pickle