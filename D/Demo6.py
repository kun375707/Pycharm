'''如何保存(腌制)数据'''
import pickle
'''导入pickle模块'''
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
     with open('man_data.txt','wb') as man_file:
        pickle.dump(man,man_file)
     with open('other_data.txt','wb') as other_file:
        pickle.dump(man,other_file)
        '''wb中b表示以二进制模式打开数据，使用dump()保存数据'''
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('picking error:'+str(perr))
    '''处理可能出现的异常'''


