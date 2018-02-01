'''self不是类'''
#类的方法与普通的函数只有一个特别的区别:
# 它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()
#self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类
class Test:
    def prt(xxxL):
        print(xxxL)
        print(xxxL.__class__)
t = Test()
t.prt()
#self 不是 python 关键字，换成其它的也是可以正常执行的