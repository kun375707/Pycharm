'''当没有":"时split()方法无法处理，所以需要利用find()方法查找冒号，找不到时会返回值-1'''
each_line = "I tell you, there's no such thing as a flying circus."
each_line.find(':')
each_line = "I tell you: there's no such thing as a flying circus."
each_line.find(':')
'''包含冒号，则返回一个正值'''
import os
os.chdir('../C/chapter3')
#if os.path.exists('sketch.txt')
'''检查此数据是否存在'''
data = open('sketch.txt')
for each_line in data:
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print('said:', end='')
        print(line_spoken, end='')
data.close()

