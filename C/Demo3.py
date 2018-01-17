'''处理异常时先尝试运行代码，再处理错误。重要代码需要利用 try 和 except 关键字来提供保护'''
import os
os.chdir('../C/chapter3')
#try:
'''确保数据存不存在'''
data = open('sketch.txt')
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)
        '''如果split()调用失败，下面三行执行并没意义，所以需要保护这四行代码'''
        print(role, end='')
        print('said:', end='')
        print(line_spoken, end='')
    except:
    #except ValueError:
    '''指定处理特殊错误类型'''
        pass
    '''如果try中出现一个错误，except会执行pass忽略掉。'''
data.close()
#except:
'''如果try中数据不存在，它会报错'''
#except IOError:
'''指定处理特殊错误类型'''