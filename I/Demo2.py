'''将数据转送到CGI脚本'''
#在web服务器上，使用标准库cgi模块提供的功能访问CGI数据
import cgi
import os
#利用Python的内置支持，使用os库查询CGI脚本的环境。
import time
import sys
import yate

print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
#查询3个环境变量,并把值赋至变量
cur_time = time.asctime(time.localtime())
print(host + ", " + addr + ", " + cur_time + ": " + method + ": ",end='', file=sys.stderr)
#在标准错误输出上显示查询的数据
form=cgi.FieldStorage()
#从CGI脚本访问发送到web服务器的数据并转换为一个字典
for each_form_item in formkeys():
    print(each_form_item + '->' + form[each_form_item].value,end='',file=sys.stderr)
    print(file=sys.stderr)
    print('OK')
    # 利用以上处理来自表单的数据，并把这些数据显示在web服务器的控制台屏幕上。