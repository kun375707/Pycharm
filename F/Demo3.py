'''简化代码'''
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
        #return(data.strip().split(','))
            '''一次性创建字典并可以使函数直接返回字典而不是列表,代码改为:'''
        templ = data.strip().split(',')
        '''创建一个临时列表来存放数据'''
        return({'Name':templ.pop(0),
                'DOB':templ.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})
        '''将确定时间的代码也变为函数的一部分'''
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return (None)
#arah = get_coach_data('sarah2.txt')
#sarah_data = {}
#sarah_data['Name'] = sarah.pop(0)
#sarah_data['DOB'] = sarah.pop(0)
#sarah_data['Times'] = sarah
#print(sarah_data['Name'] + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are:" + sarah['Times'])
'''经修改后的代码更方便简单'''