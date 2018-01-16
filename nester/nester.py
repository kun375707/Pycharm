def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
"""这是一个模块代码，提供了print_lol()函数，它可以打印列表（包括镶嵌列表）"""
Drink = ['cola', 'mike', 'coffee', 'water',
         ['num_Drink = len(Drink)',
          ['apple juice', 'orange juice']]]
#print_lol(Drink)

'''将模块发布操作：1.将代码模块放到新建文件夹中，并创建一个名为'setup.py'的文件，进行编辑 2.利用终端执行命令：python3 setup.py sdlist 3.安装到本地：sudo python setup.py install'''
'''之后导入代码，见Demo2'''
'''若将模块上传到PYPI 则需两个命令：python3 setup.py register 和 python3 setup.py sdist upload'''
'''几个BIF：list()创建一个空列表，range()根据需要生成一个指定范围的数字，enumerate()创建成对数据的一个编号列表 从0开始，int()将字符串或另一个数转换为整数，next()返回可迭代数据的  下一项'''
'''range()BIF 见Demo'''


