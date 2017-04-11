'''
向压缩档加入文件很简单, 将文件名, 文件在 ZIP 档中的名称传递给 write 方法即可.
下例 将 samples 目录中的所有文件打包为一个 ZIP 文件.
'''

import zipfile
import glob, os

# open the zip file for writing, and write stuff to it
file = zipfile.ZipFile("test.zip", "w")

for name in glob.glob("samples/*"):
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
file.close()

# open the file again, to see what's in it
file = zipfile.ZipFile("test.zip", "r")

for info in file.infolist():
    print info.filename, info.date_time, info.file_size, info.compress_size
    
    
'''
write 方法的第三个可选参数用于控制是否使用压缩.
默认为 zipfile.ZIP_STORED , 意味着只是将数据储存在档案里而不进行任何压缩.
如果安装了 zlib 模块, 那么就可以使用 zipfile.ZIP_DEFLATED 进行压缩.
'''