'''使用class定义类'''
class Athlete:
    '''创建一个名为Athlete的类'''
    def __init__(self, a_name, a_dob = None, a_times = []):
        '''每个定义的类都有一个特殊的方法_init_()并且需要self作为第一个参数,可以通过这个方法控制如何初始化对象'''
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    '''初始化这3个属性，使用所提供的参数数据为3个类属性赋值'''
    def top3(self):
        return(sorted(set([sanitize(t)for t in self.times]))[0:3])
'''定义一个新方法,调用这个方法返回最快时间'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':'in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)
def get_coach_data(filename):
        try:
            with open(filename)as f:
                data = f.readline()
            templ = data.strip().split(',')
        #return ({'Name': templ.pop(0),
                 #'DOB': templ.pop(0),
                 #'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
            '''将以上三行代码修改为如下:'''
            return(Athlete(templ.pop(0),templ.pop(0),templ))
        except IOError as ioerr:
            print('File error:'+ str(ioerr))
            return (None)
sarah = get_coach_data('sarah2.txt')
#print(sarah['Name'] + "'s fastest times are:" + sarah['Times'])
'''用使用点记法访问数据改为如下:'''
print( sarah.name + "'s fastest times are:" + str(sarah.top3()))
'''调用top3()方法，利用str()把结果转换为一个字符串'''



