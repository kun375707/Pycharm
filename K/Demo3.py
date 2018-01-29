'''列表推导'''
times = [t for t in row_data['Marathon'].keys()]
#将代码分开如下
        times = []
        #首先是一个空列表
        for each_t in row_data['Marathon'].keys():
            #将字典的链接转换为一个空列表
            times.append(each_t)
            #每次迭代时，将一个时间值追加到'times'列表
headings = [h for h in sorted(row_data['10mi'].values(),reverse=True)]
time = [t for t in row_data['20k'].keys() if row_data['20k'][t]] == '79.3'
#之后要得到用户输入
#input()BIF可以在屏幕上显示一个提示语，然后接收键盘输入，并把输入的内容作为一个字符串返回给代码。
distance_run = input('Enter the distance attempted: ')
recorded_time = input('Enter the recorded time: ')
predicted_distance = input('Enter the distance you want a prediction for: ')
#获取输入会产生一个问题，输入的时间值在表格的两个值之间无法找到

