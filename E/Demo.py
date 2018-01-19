'''列表排序'''
with open('james.txt')as jaf:
    '''打开文件'''
    data = jaf.readline()
    '''读取数据'''
james = data.strip().split(',')
'''这是一个方法链,先删除不想要的空白符，再创建列表来分离'''
with open('julie.txt')as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt')as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt')as saf:
    data = saf.readline()
sarah = data.strip().split(',')
print(james)
print(julie)
print(mikey)
print(sarah)
'''排序分为复制排序和原地排序，使用sort()方法和sorted()BIF默认升序排列，若以降序排列需传入参数 reverse=true'''
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
'''复制排序如上，原数据的顺序依旧保留，只是对一个副本排序。而原地顺序则相反，原顺序会被覆盖。'''
'''排序时，短横线>点号>冒号。所以需使用清理函数 sanitize()进行转换'''





