'''如何恢复数据'''
import pickle
import Demo4
new_man=[]
'''创建一个新列表来解除保存(腌制)的数据'''
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
        '''使用load()来恢复数据'''
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('picking error:'+str(perr))
Demo4.print_lol(new_man)
'''利用Demo4代码块来标准输出'''
