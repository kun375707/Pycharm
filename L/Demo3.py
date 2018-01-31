'''re.search方法'''
#re.search 扫描整个字符串并返回第一个成功的匹配
re.search(pattern, string, flags=0)
import re
print(re.search('www', 'www.xxx.com').span())
# 在起始位置匹配
print(re.search('com', 'www.xxx.com').span())
# 不在起始位置匹配
import  re
line = "Cats are smarter than dogs";
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")