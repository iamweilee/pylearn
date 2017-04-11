'''
ע���߳�֧��ģ���ǿ�ѡ��, �п�����һЩ Python �������в�����.

ִ�� Python �����ʱ��, �ǰ��մ���ģ�鶥������ִ�е�.
ѭ�������ظ�ִ�в��ִ���, �����ͷ����Ὣ������ʱ�ƽ����������һ����.
ͨ���߳�, ��ĳ��������ͬʱ����������. ÿ���̶߳������Լ��Ŀ�����.
�����������һ���߳�����ļ���ȡ����, �������Ļ�������.
Ϊ�˱�֤�����߳̿���ͬʱ������ͬ���ڲ�����, Python ʹ���� globalinterpreter lock (ȫ�ֽ�������).
��ͬһʱ��ֻ������һ���߳�ִ��Python ����;
Python ʵ�������Զ�����һ�κ̵ܶ�ʱ����л����¸��߳�ִ��, ���ߵȴ�һ���߳�ִ��һ����Ҫʱ��Ĳ���(����ȴ�ͨ�� socket ���������, ���Ǵ��ļ��ж�ȡ����).
ȫ������ʵ�ϲ����ܱ���������е�����.
����̳߳��Է�����ͬ�����ݻᵼ���쳣״̬.

�������µĴ���:

def getitem(key):
    item = cache.get(key)
    if item is None:
        # not in cache; create a new one
        item = create_new_item(key)
        cache[key] = item
    return item
    
    
�����ͬ���߳��Ⱥ�ʹ����ͬ�� key ��������� getitem ����, ��ô���Ǻܿ��ܻᵼ����ͬ�Ĳ����������� create_new_item.
���ʱ��������û������, ����ĳЩʱ��ᵼ�����ش���.
���������ʹ�� lock objects ��ͬ���߳�.
һ���߳�ֻ��ӵ��һ�� lock object, �����Ϳ���ȷ��ĳ��ʱ��ֻ��һ���߳�ִ�� getitem ����.
'''

'''
�ڴ���ִ�����ϵͳ��, ÿ��������������Ľ���( process ) ��ִ��.
����ͨ���� shell �м��������ֱ���ڲ˵���ѡ����ִ��һ������/����.
Python ��������һ���ű���ִ��һ���µĳ���.
��������غ���ͨ�� os ģ�鶨��.
'''

'''
(��ѡ) threading ģ��Ϊ�߳��ṩ��һ���߼��ӿ�, �� ���� ��ʾ.
��Դ�� Java ���߳�ʵ��.
�͵ͼ��� thread ģ����ͬ, ֻ�����ڱ��������ʱ�����߳�֧�ֲſ���ʹ���� .
��ֻ��Ҫ�̳� Thread ��, ����� run ����, �Ϳ��Դ���һ ���µ��߳�.
ʹ��ʱ���ȴ��������һ������ʵ��, Ȼ����� start ����.
����ÿ��ʵ���� run �����������������Լ����߳���.
'''

import threading
import time, random

class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0
        
    def increment(self):
        self.lock.acquire() # critical section
        self.value = value = self.value + 1
        self.lock.release()
        return value
    
counter = Counter()

class Worker(threading.Thread):
    #def __init__(self):
    #    threading.Thread.__init__(self)
        
    def run(self):
        for i in range(10):
            # pretend we're doing something that takes 10?00 ms
            value = counter.increment() # increment global counter
            time.sleep(random.randint(10, 100) / 1000.0)
            print self.getName(), "-- task", i, "finished", value

#
# try it
for i in range(10):
    Worker().start() # start a worker