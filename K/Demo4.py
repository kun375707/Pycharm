'''搜索最接近的匹配'''
def find_closest(look_for, target_data):
#该函数完成一个简单的线性搜索,返回target_data中与look_for参数最接近的值
    def whats_the_difference(first, second):  #嵌套函数
        if first == second:
            return(0)
        elif first > second:
            return(first - second)
        else:
            return(second - first)
#这个嵌套函数给定两个值,这个函数会返回二者之差
    max_diff = 9999999
    for each_thing in target_data:
        diff = whats_the_difference(each_thing, look_for)
        if diff == 0:
            found_it = each_thing
            break
        elif diff < max_diff:
            max_diff = diff
            found_it = each_thing
    return(found_it)
#这是运行数据会出现错误，见Demo5