'''使用字典关联数据'''
'''字典是python中的内置数据结构,允许将数据与键而不是数字关联。
   字典不会维持插入的顺序,重点维护关联关系'''
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
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return (None)
sarah = get_coach_data('sarah2.txt')
#(sarah_name, sarah_dob) = sarah.pop(0),sarah.pop(0)
#print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
'''将如上两行代码改为:'''
sarah_data = {}
'''创建一个空字典,还可用 XX = dict()来创建，这是一个工厂函数。注意XX这个字典中的键与值是同时创建的'''
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name'] + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
'''字典和列表区别在于字典更容易地确定和控制哪些标签数据与哪些时间数据关联，但代码会增加更多'''