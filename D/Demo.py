import os
os.chdir('../D')
man = []
other = []
try:
    '''确保数据存不存在'''
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            '''如果split()调用失败，下面三行执行并没意义，所以需要保护这四行代码'''
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            '''指定处理特殊错误类型'''
            pass
    '''如果try中出现一个错误，except会执行pass忽略掉。'''
    data.close()
except IOError:
    '''指定处理特殊错误类型'''
    print('The datafile is missing!')
#print(man)
#print(other)
'''写入文件操作如下'''
try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')
    '''写入上面两个文件'''
    print(man, file=man_file)
    print(other, file=other_file)
    '''如果上面两行代码错误，就会使下面两行无法执行，故使用try/finally语句，改为如下'''
    #man_file.close()
    #other_file.close()
except IOError:
    print('File error')
finally:
    man_file.close()
    other_file.close()
'''发生错误，finally下的代码也会执行'''