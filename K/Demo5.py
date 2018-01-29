'''时间问题'''
#CSV中的值都是字符串，find_closest()函数处理的是数字，导致混乱。
#时间为秒转换模块
import time

def format_time(time_string):
#确保所有时间都采用“HH:MM:SS"格式 有助于保证将时间转换为秒数时更为简单
    tlen = len(time_string)
    if tlen < 3:
        original_format = '%S'
    elif tlen < 6:
        original_format = '%M:%S'
    else:
        original_format = '%H:%M:%S'
    time_string = time.strftime('%H:%M:%S', time.strptime(time_string, original_format))
    return(time_string)

def time2secs(time_string):
#给定一个”时间字符串“，转换为一个秒数值
    time_string = format_time(time_string)
    (hours, mins, secs) = time_string.split(':')
    seconds = int(secs) + (int(mins)*60) + (int(hours)*60*60)
    return(seconds)

def secs2time(seconds):
#将一个秒数值转换为”时间字符串“
    return(time.strftime('%H:%M:%S', time.gmtime(seconds)))
#定义一个新函数，它取两个参数，要查找的时间和所搜索的时间列表，把最接近的时间作为一个字符串返回：
from find_it import find_closest
from tm2secs2tm import time2secs, secs2time
#导入代码
def find_nearest_time(look_for, target_data):
    #取两个参数，一个是时间字符串，以及一个时间字符列表
    what = time2secs(look_for)
    #将要查找的时间字符串转换为等价的秒数值
    where = [time2secs(t) for t in target_data]
    #将时间字符串行转换为秒数
    res = find_closest(what, where)
    #调用find_closest()并提供已转换的数据
    return(secs2time(res))
#转换后，将最接近的匹配结果返回给调用代码