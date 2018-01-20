'''定制数据'''
'''写入第五章中的代码'''
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
'''增加如下代码'''
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0),sarah.pop(0)
'''pop()调用会删除前面两个数据值'''
print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
'''print中的定制消息会得到想要的结果'''
