'''
dir 返回由给定模块, 类, 实例, 或其他类型的所有成员组成的列表. 这可能在交互式 Python 解释器下很有用, 也可以用在其他地方.
'''

def dump(value):
    print value, "=>", dir(value)
    
import sys
dump(0)
dump(1.0)
dump(0.0j) # complex number
dump([]) # list
dump({}) # dictionary
dump("string")
dump(len) # function
dump(sys) # module