'''访问私有变量'''
class JustCounter:
    __secretCount = 0
    # 私有变量
    publicCount = 0
    # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
    def count2(self):
        print (self.__secretCount)

counter = JustCounter()
counter.count()
# 在类的对象生成后,调用含有类私有属性的函数时就可以使用到私有属性.
counter.count()
#第二次同样可以.
print(counter.publicCount)
print(counter._JustCounter__secretCount)
# 不改写报错，实例不能访问私有变量
try:
    counter.count2()
except IOError:
    print ("不能调用非公有属性!")
else:
    print ("ok!" )
'''新式类和经典类的区别'''
class A:
   def foo(self):
      print('called A.foo()')
class B(A):
   pass
class C(A):
   def foo(self):
      print('called C.foo()')
class D(B, C,object):
   pass

if __name__ == '__main__':
   d = D()
   d.foo()
#D继承了object和不继承程序输出不一样，
# 继承object会调用C类的 foo，否则会调用A的,并出现报错