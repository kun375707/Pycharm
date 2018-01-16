import nester
'''导入代码'''
fruit = ['aplle','orange','watermelon','pear']
#print_lol(fruit)
'''会有一个nameerror，这时需要一个命名空间，如下。若使用from nester import print_lol会把当前函数增加到命名空间 就不必使用命名空间了'''
nester.print_lol(fruit)