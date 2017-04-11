'''
(只用于 Unix) pipes 模块提供了 "转换管道 (conversion pipelines)" 的支持.
你可以创建包含许多外部工具调用的管道来处理多个文件.
如 下例 所示.
'''

import pipes

t = pipes.Template()

# create a pipeline
# 这里 " - " 代表从标准输入读入内容
t.append("sort", "--")
t.append("uniq", "--")

# filter some text
# 这里空字符串代表标准输出
t.copy("samples/sample.txt", "")


'''
貌似 windows 高级版本 (windows 7、windows 8 以上版本) 支持 commands, 可能是因为 windows 自带了 shell 吧.
但为何输出却是乱码呢......
'''