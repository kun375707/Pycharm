'''正则表达式'''
#正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配
re.match(pattern, string, flags=0)
#re.match函数: 尝试从字符串的起始位置匹配一个模式，
# 如果不是起始位置匹配成功的话，match()就返回none
import re
print(re.match('www', 'www.xxx.com').span())
# 在起始位置匹配
print(re.match('com', 'www.xxx.com'))
# 不在起始位置匹配

import re
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#正则表达式 (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符
#(.*?) 第二个匹配分组，.*? 后面多个问号只匹配符合条件的最少字符
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")