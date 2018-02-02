'''类属性与方法'''
#类的私有属性:__private_attrs：声明该属性为私有，不能在类的外部被使用或直接访问
# 在类内部的方法中使用时 self.__private_attrs。
class JustCounter:
    __secretCount = 0
    # 私有变量
    publicCount = 0
    # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)
# 运行后会报错，实例不能访问私有变量
#但可以使用 object._className__attrName 访问属性，修改代码如下
print(counter._JustCounter__secretCount)