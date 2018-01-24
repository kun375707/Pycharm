'''编写android最后脚本程序'''
import android
import json
import time
from urllib import urlencode
from urllib2 import urlopen

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

athlete_names = sorted(json.loads(send_to_server(web_server + get_name_cgi)))
# 将web请求发送给服务器，把json相应转换为一个有序列表
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
    selected_name = athlete_names[selected_index]
    athlete = json.loads(send_to_server(web_server + get_data_cgi, {'athlete': selected_name}))
    athlete_title = athlete['name'] + ' (' + athlete['dob'] + '), top 3 times: '
    app.dialogCreateAlert(athlete_title)
    app.dialogSetItems(athlete['top3'])
    app.dialogSetPositiveButtonText('OK')
    app.dialogShow()
    resp = app.dialogGetResponse().result

status_update(quit_msg)
# 显示退出消息