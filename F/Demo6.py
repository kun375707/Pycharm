'''继承Python的内置list类'''
#class NamedList(list):
'''提供一个类名，新的类将派生这个类'''
    #def __init__(self, a_name):
        #list.__init__([])
'''初始化所派生的类'''
        #self.name = a_name
'''将参数赋至属性'''
'''所以之前的代码可修改为:'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':'in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob = None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t)for t in self]))[0:3])
def get_coach_data(filename):
        try:
            with open(filename)as f:
                data = f.readline()
            templ = data.strip().split(',')
            return(AthleteList(templ.pop(0),templ.pop(0),templ))
        except IOError as ioerr:
            print('File error:'+ str(ioerr))
            return (None)
sarah = get_coach_data('sarah2.txt')
print( sarah.name + "'s fastest times are:" + str(sarah.top3()))
'''增加一个对象实例来测试新的代码'''
vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1.21','2.22'])
print(vera.top3())
