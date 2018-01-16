#def print_lol(the_list, level):
#def print_lol(the_list, level=0):
    #'''为函数设置一个缺省值，使其变为可选函数'''
def print_lol(the_list,indent=False ,level=0):
    '''为函数再添加一个变量indent，可控制缩进特性'''
    for each_item in the_list:
        if isinstance(each_item, list):
            #print_lol(each_item, level+1)
            print_lol(each_item,indent,level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                 '''利用range()来让列表缩进指定书目的制表符'''
                print('\t',end = '')
                '''每一层缩进显示一个TAB制表符,而不是换行'''
            print(each_item)
Drink = ['cola', 'mike', 'coffee', 'water',
         ['num_Drink = len(Drink)',
          ['apple juice', 'orange juice']]]
#print_lol(Drink,0)
#print_lol(Drink)
'''没有指定第二个参数，使用缺省值'''
#print_lol(Drink,2)
print_lol(Drink,True)
'''为第二个参数提供True来打开缩进'''
