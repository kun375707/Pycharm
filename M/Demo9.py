'''通过CGI程序传递checkbox数据'''
#heckbox用于提交一个或者多个选项数据

# 引入 CGI 处理模块
import cgi, cgitb
# 创建 FieldStorage的实例
form = cgi.FieldStorage()
# 接收字段数据
if form.getvalue('google'):
   google_flag = "是"
else:
   google_flag = "否"

if form.getvalue('runoob'):
   runoob_flag = "是"
else:
   runoob_flag = "否"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title> CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 你是否选择了 : %s</h2>" % runoob_flag)
print("<h2> Google 是否选择了 : %s</h2>" % google_flag)
print("</body>")
print("</html>")