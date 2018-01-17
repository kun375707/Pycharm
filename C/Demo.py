import os
os.getcwd()
'''查询当前工作的目录'''
os.chdir('../C/chapter3')
'''切换指定目录'''
data = open('sketch.txt')
print(data.readline(),end='')
'''获取一个数据行'''
print(data.readline(),end='')
data.seek(0)
'''将文件返回起始位置'''
for each_line in data:
    print(each_line,end='')
data.close()
data = open('sketch.txt')
for each_line in data:
    #(role, line_spoken) = each_line.split(':')
    '''利用split()方法分离数据'''
    (role, line_spoken) = each_line.split(':',1)
    '''增加第二个参数来解决单参数出现的报错'''
    print(role, end='')
    print('said:', end='')
    print(line_spoken, end='')
data.close()
'''此时还是会有报错，对付报错有两种方法：1.增加逻辑(见demo2) 2.发生时，处理异常(见Demo3)'''
'''综合两种方法第二种还是好于第一种，第一种需要先考虑大量的逻辑和代码，而第二种方法更为直接。'''



