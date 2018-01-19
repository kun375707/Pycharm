'''用集合删除重复项的重复代码'''
'''python集合中的数据项是无序的，不允许重复，重复项会被忽略。
   这里要是使用set()BIF来创建一个空集合，它是一个工厂函数。
   工厂函数用于创建某种类型的新数据项'''
#james = sorted([sanitize(t) for t in james])
'''之前的代码可更改为:'''
#print(sorted(set([sanitize(t) for t in james]))[0:3])
'''为了使代码更简便可将Demo5中4组with语句 定义一个函数：'''
def get_coach_data(filename):
    '''接收一个文件名作为唯一的参数'''
    try:
        with open(filename)as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return (None)
'''添加try/except异常处理代码,当有错误信息时，会返回None'''
james = get_coach_data('james.txt')
'''调用如上函数'''
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
from Demo2 import sanitize
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
