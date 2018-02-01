'''创建实例对象以及访问属性'''
#创建实例对象
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
#访问属性
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
#结合5 6 7:
class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
#可以添加，删除，修改类的属性，如下：
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性
#也可以使用以下函数的方式来访问属性：
hasattr(emp1, 'age')
# 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')
# 返回 'age' 属性的值
setattr(emp1, 'age', 8)
# 添加属性 'age' 值为 8
delattr(emp1, 'age')
# 删除属性 'age'