'''用with处理文件'''
try:
    data = open('missing.txt')
    print(data.readline(),end='')
except IOError as err:
    print('File error:' + str(err))
finally:
    if 'data' in locals():
        data.close()
'''利用 with 就不用需要 finally 可将代码改为如下'''
try:
    with open('missing.txt')as data:
        print(data.readline(),end='')
except IOError as err:
    print('File error:' + str(err))
'''利用 with 重写(Demo)中写入文件的代码'''
import os
os.chdir('../D')
man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
try:
    with open('man_data.txt','w')as man_file:
        print(man,file=man_file)
    with open('other_data.txt','w')as other_file:
        print(other,file=other_file)
except IOError as err:
    print('File error:'+str(err))

with open('man_data.txt') as mdf:
    print(mdf.readline())
    '''利用with打开其中一个文件，并不需要关闭操作，with会自动完成'''


