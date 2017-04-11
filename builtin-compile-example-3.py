'''
使用下例中的类可以在程序执行时实时地生成代码. write 方法用于添加代码, indent 和 dedent 方法用于控制缩进结构. 其他部分交给类来处理.
'''

import sys, string
class CodeGeneratorBackend:
    "Simple code generator for Python"
    
    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0
    
    def end(self):
        self.code.append("") # make sure there's a newline at the end
        return compile(string.join(self.code, "\n"), "<code>", "exec")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1 # in 2.0 and later, this can be written as: self.level += 1 

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1 # or: self.level -= 1
#
# try it out!
c = CodeGeneratorBackend()
c.begin()
c.write("for i in range(5):")
c.indent()
c.write("print 'code generation made easy!'")
c.dedent()
exec c.end()