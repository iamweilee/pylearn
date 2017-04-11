'''
�� 2.0 ���Ժ�汾, shuffle �����������ڴ���һ���б������ (Ҳ��������һ�����б�����ȫ����).
���� չʾ������ھɰ汾��ʵ�ָú���.
'''

import random

try:
    # available in 2.0 and later
    shuffle = random.shuffle
except AttributeError:
    def shuffle(x):
        for i in xrange(len(x)-1, 0, -1):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = int(random.random() * (i+1))
            x[i], x[j] = x[j], x[i]
            
            
cards = range(52)
shuffle(cards)
myhand = cards[:5]
print myhand

'''
xrange �÷��� range ��ȫ��ͬ, ����ͬ�������ɵĲ���һ��list����, ����һ��������.
�������ʾ������֪��: Ҫ���ɺܴ���������е�ʱ��, ��xrange���range�����źܶ�, ��Ϊ����Ҫһ�����Ϳ���һ��ܴ���ڴ�ռ�.

xrange �� range �����������϶�����ѭ����ʱ����.

for i in range(0, 100): 
    print i 

for i in xrange(0, 100): 
    print i 

����������Ľ������һ����, ʵ�����кܶ಻ͬ, range��ֱ������һ��list����, ��xrange�򲻻�ֱ������һ��list, ����ÿ�ε��÷������е�һ��ֵ.
����xrange��ѭ�������ܱ�range��, �����Ƿ��غܴ��ʱ��.
������xrange��, ��������Ҫ����һ���б�.
'''