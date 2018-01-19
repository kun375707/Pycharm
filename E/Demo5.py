'''删除重复项'''
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
james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])
'''创建一个空列表'''
unique_james = []
for each_t in james:
    '''进行迭代处理'''
    if each_t not in unique_james:
        unique_james.append(each_t)
        '''将数据项追加到新列表中'''
print(unique_james[0:3])
'''从列表分片得到前3个数据项'''
unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])
unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])
unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])
