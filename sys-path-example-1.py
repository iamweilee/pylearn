'''
sys ģ���ṩ����ຯ���ͱ��������� Python ����ʱ�����Ĳ�ͬ����.
'''

'''
path �б���һ����Ŀ¼�����ɵ��б�, Python ���в�����չģ��( Python Դģ��, ����ģ��,���߶�������չ).
���� Python ʱ,����б�Ӹ����ڽ�����, PYTHONPATH ��������������, �Լ�ע���( Windows ϵͳ)�Ƚ��г�ʼ��.
������ֻ��һ����ͨ���б�, ������ڳ����ж������в���, �� ���� ��ʾ.
'''

import sys

print "path has", len(sys.path), "members"
# add the sample directory to the path
sys.path.insert(0, "samples")

import sample
# nuke the path
sys.path = []
import random # oops!