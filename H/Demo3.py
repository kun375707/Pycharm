'''编写andorod应用第二步'''
#由于Json库只能处理Python的内置类型,无法处理athletelist对象
#故需在athletelist模版中增加一个方法,将数据转换为字典(被Json支持)，再把字典发回应用
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)
    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])

    @property
    def to_dict(self):
        return {'name': self.name,
                'dob': self.dob,
                'top3': self.top3()}

