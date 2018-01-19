'''定义清理函数，将':'和'-' 转为为点号。'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':'in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    '''分解字符串，抽出分钟和秒钟'''
    return(mins + '.' + secs)