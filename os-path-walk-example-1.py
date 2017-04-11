'''
walk 函数会帮你找出一个目录树下的所有文件 (如下例所示).
它的参数依次是目录名, 回调函数, 以及传递给回调函数的数据对象.
'''

import os

def callback(arg, directory, files):
    for file in files:
        print os.path.join(directory, file), repr(arg)
        
        
os.path.walk(".", callback, "secret message")