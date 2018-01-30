'''移植到Android'''
import time
import android
from find_it import find_closest
from tm2secs2tm import time2secs, secs2time, format_time  #完成导入

def find_nearest_time(look_for, target_data):  #包含”find_nearest()“函数
    what = time2secs(look_for)
    where = [time2secs(t) for t in target_data]
    res = find_closest(what, where)
    return(secs2time(res))

distances = [ '2mi', '5k', '5mi', '10k', '15k', '10mi', '20k',  #声明常量
                '13.1mi', '25k', '30k', 'Marathon' ]
hello_msg = "Welcome to the Marathon Club's App"
quit_msg = "Quitting the Marathon Club's App."

row_data = {}

with open('/sdcard/sl4a/scripts/PaceData.csv') as paces:
    #打开一个特定文件夹，得到并预处理CVS数据
    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0)
    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_headings)):
            inner_dict[format_time(row[i])] = column_headings[i]
        row_data[row_label] = inner_dict

app = android.Android()
#创建android应用对象，并包含你的辅助函数
def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

def do_dialog(title, data, func, ok='Select', notok='Quit'):
    app.dialogCreateAlert(title)
    func(data)
    app.dialogSetPositiveButtonText(ok)
    if notok:
        app.dialogSetNegativeButtonText(notok)
    app.dialogShow()
    return(app.dialogGetResponse().result)

status_update(hello_msg)

resp = do_dialog("Pick a distance", distances, app.dialogSetSingleChoiceItems)
#向用户显示用户界面，并交互处理
if resp['which'] in ('positive'):
    distance_run = app.dialogGetSelectedItems().result[0]
    distance_run = distances[distance_run]
    #将选择的距离标签赋至'distance_run'
    recorded_time = app.dialogGetInput("Enter a " + distance_run + " time:",
                                           "Use HH:MM:SS format:").result
    closest_time = find_nearest_time(format_time(recorded_time), row_data[distance_run])
    closest_column_heading = row_data[distance_run][closest_time]
    #得出要使用哪个标题
    resp = do_dialog("Pick a distance to predict", distances, app.dialogSetSingleChoiceItems)
    #要求用户从标签列表选择一个要预测的距离
    if resp['which'] in ('positive'):
        predicted_distance = app.dialogGetSelectedItems().result[0]
        predicted_distance = distances[predicted_distance]
        #如下查找预测时间
        prediction = [k for k in row_data[predicted_distance].keys()
                          if row_data[predicted_distance][k] == closest_column_heading]
        do_dialog('The predicted time running ' + predicted_distance + ' is: ',
                             prediction, app.dialogSetItems, "OK", None)
status_update(quit_msg)