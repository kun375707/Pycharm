'''设计Web应用第一步 建立模型'''
import pickle
from athletelist import AthleteList
#意思是从athletelist.py模块中导入AthleteList

def get_coach_data(filename):
    try:
        with open(filename)as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return (None)

def put_to_store(files_list):
    all_athletes = {}
    # 定义字典，用于存储运动员对象
    for each_file in files_list:
        # get_coach_data(each_file)打开文件列表中的每一个文件，
        # 并将其转换成AthleteList对象。
        # 最后，将AthleteList对象存入all_athletes字典。
        #每个选手的名字作为字典的'键'，'值'是对象实例
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        # 打开athletes.pickle文件，将字典 all_athletes存入其中。
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        # 打开athletes.pickle文件，它是一个字典
        # 然后，将其赋值给字典all_athletes。
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return (all_athletes)
the_files = ['sarah.txt','james.txt','mikey.txt','julie.txt']
data = put_to_store(the_files)
#现在会生成一个athletes.pickle文件，这个文件是一个二进制文件，
#访问他需要使用put_to_store()或get_from_store()函数返回字典
for each_athlete in data:
    print(data[each_athlete].name + '' + data[each_athlete].dob)
    #通过访问name和dob属性来得到数据
data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + '' + data_copy[each_athlete].dob)
    #使用get_from_store()函数将腌制的数据加载到另一个字典中，重复代码生成的数据与上面相同


