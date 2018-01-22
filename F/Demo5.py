'''增加方法来完成更多的工作'''
class Athlete:
    def __init__(self, a_name, a_dob = None, a_times = []):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(t)for t in self.times]))[0:3])

    def add_time(self,time_value):
        self.times.append(time_value)
        '''增加add_time()方法增加新的计时值'''
    def add_times(self,list_of_times):
        self.times.extend(list_of_times)
        '''增加add_times()方法来增加一个时间列表'''

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
            return(Athlete(templ.pop(0),templ.pop(0),templ))
        except IOError as ioerr:
            print('File error:'+ str(ioerr))
            return (None)
sarah = get_coach_data('sarah2.txt')
print( sarah.name + "'s fastest times are:" + str(sarah.top3()))
'''增加一个对象实例来测试新的代码'''
vera = Athlete('vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1.21','2.22'])
print(vera.top3())