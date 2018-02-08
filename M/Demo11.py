'''通过CGI程序传递下拉数据'''
# 引入 CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('dropdown'):
   dropdown_value = form.getvalue('dropdown')
else:
   dropdown_value = "没有内容"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title> CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 选中的选项是 : %s</h2>" % text_content)
print("</body>")
print("</html>")