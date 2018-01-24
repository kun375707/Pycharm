'''在Android数据输入'''
#创建一个android应用，与用户交互两次。第一次对话框要求用户确认web服务器使用能够的web地址和端口。
# 假设用户在这个对话框上点击ok按钮，会弹出第二个对话框，请求用户输入要发送到服务器的计时值。
import android
from urllib import urlencode
from urllib2 import urlopen

server_title  = 'Which server should I use?'
server_msg    = "Please confirm the server address/name to use for your athlete's timing data:"
timing_title  = 'Enter data'
timing_msg    = 'Provide a new timing value:'
web_server    = 'http://10.10.138.89:8080'
add_time_cgi  = '/cgi-bin/add_timing_data.py'
app = android.Android()

def send_to_server(url, post_data=None):
    if post_data:
        page = urllib.urlopen(url, urllib.urlencode(post_data))
    else:
        page = urllib.urlopen(url)
    return(page.read().decode("utf8"))

resp = app.dialogGetInput(server_title, server_msg, web_server).result
#第一个对话框请求用户确认要使用的web地址和接口
if resp is not None:
    #如果用户没有点击取消按钮
    web_server = resp
    resp = app.dialogGetInput(timing_title, timing_msg).result
    #第二个对话框要求输入一个新的计时值
    if resp is not None:
        new_time = resp
        send_to_server(web_server + add_time_cgi, {'TimingValue': new_time})
        #应用会将数据发送到web服务器