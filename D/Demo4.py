'''修改之前'nester'模块中的代码来标准输出'''
import sys
def print_lol(the_list,indent=False ,level=0,fh=sys.stdout):
    '''增加第4个参数用来标识将数据写入哪个位置，一定要提供缺省值sys.stdout'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,indent,level + 1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='',file=fh)
                    '''增加调用参数'''
            print(each_item,file=fh)
'''此模块为新的nester代码模块'''

