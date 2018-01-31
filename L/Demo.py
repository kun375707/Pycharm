'''处理作用域'''
name = "Head First Python"
#这是一个名为'name'的全局变量
def what_happens_here():
    print(name)
    name = name + "is a great book!"
    print(name)
    #这是一个读写全局变量'name'的函数
what_happens_here()
print(name)
#如果运行这个程序，则会出现报错,要访问和修改一个全局变量修改如下:

name = "Head First Python"
def what_happens_here():
    print(name)
    global name
    name = name + "is a great book!"
    print(name)
    #这是一个读写全局变量'name'的函数
what_happens_here()
print(name)
