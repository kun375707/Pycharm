'''列表推导'''
#clean_mikey = []
#for each_t in mikey:
    #clean_mikey.append(sanitize(each_t))
'''如上一个列表转换为新列表时需要四步:
 1.创建一个新列表
 2.迭代处理原列表的数据 
 3.每次迭代时进行转换 
 4.将转换后的数据加到新列表中'''
#clean_mikey = [sanitize(each_t)for each_t in mikey]
'''如上为列表推导过程，缩减为只有一行代码'''

from Demo2 import sanitize
'''导入Demo2中的sanitize函数'''
with open('james.txt')as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt')as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt')as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt')as saf:
    data = saf.readline()
sarah = data.strip().split(',')
print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))
'''如上为经过列表推导的Demo3会直接显示到屏幕上,注意不能这样使用函数链 sorted(sanitize(t)) 因为一次只会转换一个数据。而sorted()希望对整个列表排序。'''


