'''方法重写'''
#如果父类方法的功能不能满足需求，可以在子类重写父类的方法
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')

c = Child()
# 子类实例
c.myMethod()
# 子类调用重写方法
'''基础方法重写'''
#__init__ ( self [,args...] )构造函数  调用方法: obj = className(args)
#__del__( self ) 析构方法 ,删除一个对象  调用方法 : del obj
#__repr__( self )转化为供解释器读取的形式  调用方法 : repr(obj)
#__str__( self )用于将值转化为适于人阅读的形式  调用方法 : str(obj)
#__cmp__ ( self, x )对象比较  调用方法 : cmp(obj, x)