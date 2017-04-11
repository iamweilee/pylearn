'''
因为 Python 在检查局部名称空间和模块名称空间前不会检查内建函数, 所以
有时候你可能要显式地引用 _ _builtin_ _ 模块. 下例重载了
内建的 open 函数. 这时候要想使用原来的 open 函数, 就需要脚本显式地指
明模块名称.
'''

def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in("GIF87", "GIF89"):
        raise IOError, "not aGIF file"
    file.seek(0)
    return file

fp = open("samples/sample.png")
print len(fp.read()), "bytes"
fp = open("samples/sample.jpg")
print len(fp.read()), "bytes"

'''
[!Feather 注: 明白这个 open()函数是干什么的么? 检查一个文件是否是 GIF文件,
一般如这类的图片格式都在文件开头有默认的格式.
另外打开文件推荐使用 file()而不是 open() , 虽然暂时没有区别]
'''