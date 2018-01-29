'''将文件中各个时间存储为字典'''
row_data = {}

with open('PaceData.csv') as paces:

    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0)

    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        inner_dict = {}
        #创建另一个空字典
        for i in range(len(column_headings)):
            inner_dict[row[i]] = column_headings[i]
            #'每次迭代时，i将是当前列号'
            #将列标题与行中的时间值关联
        row_data[row_label] = inner_dict
        #填充字典后，将其赋至“row_data”中相应行标签。