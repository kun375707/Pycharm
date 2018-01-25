'''修改Android应用'''
import android
import json
import time
from urllib import urlencode
from urllib2 import ur

hello_msg = "Welcomd to Coach Kelly's Timing App"
list_title = "Here is your list of athletes:"
quit_msg = "Quitting Coach Kelly's App."
web_server = "http://192.168.115.1:8080"
get_name_cgi = "/cgi-bin/generate_names.py"
get_data_cgi = "/cgi-bin/generate_data.py"


def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return page.read().decode('utf8')
"""该函数取一个url和一些可选数据，向web服务器发送一个web请求，web响应返回给调用者"""

app = android.Android()


def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)
    """显示简短消息提示"""

status_update(hello_msg)
# 显示欢迎消息

#athlete_names = sorted(json.loads(send_to_server(web_server + get_name_cgi)))
# 将web请求发送给服务器，把json相应转换为一个有序列表
athletes = sorted(json.loads(send_to_server(web_server + get_names_cgi)))
athlete_names = [ath[0] for ath in athletes]
#只从列表的列表中抽取选手名字
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()
# 创建一个包含两个按钮的对话框

resp = app.dialogGetResponse().result
# 等待用户点击一个按钮，把结果赋给resp
if resp['which'] in ('positive'):
    selected_index = app.dialogGetSelectedItems().result[0]
    which_athlete = athletes[selected_athlete][1]
    #确定与所选选手关联的ID
    athlete = json.loads(send_to_server(web_server + get_data_cgi, {'athlete': selected_name}))
    athlete_title = athlete['name'] + ' (' + athlete['dob'] + '), top 3 times: '
    app.dialogCreateAlert(athlete_title)
    app.dialogSetItems(athlete['top3'])
    app.dialogSetPositiveButtonText('OK')
    app.dialogShow()
    resp = app.dialogGetResponse().result

if resp['which'] in ('positive'):
    pass
elif resp['which'] in ('negative'):
    timing_title = 'Enter a new time'
    timing_msg = 'Provide a new timing value ' + athlete['Name'] + ': '
    add_time_cgi = '/cgi-bin/add_timing_data.py'
#定义对话框的标题，并指定要把数据发送到哪个CGI
    resp = app.dialogGetInput(timing_title, timing_msg).result
    #显示对话框并等待用户输入
if resp is not None:
    new_time = resp
    send_to_server(web_server + add_time_cgi, {'Time': new_time, 'Athlete': which_athlete})

status_update(quit_msg)
# 显示退出消息
