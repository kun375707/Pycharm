'''面向对象'''
#创建类
class Employee:
    '所有员工的基类'
    empCount = 0
#empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
#__init__()方法很特殊，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
#self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)