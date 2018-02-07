'''GET和POST方法'''
#使用GET方法传输数据
#以下是一个简单的URL，使用GET方法向hello_get.py程序发送两个参数：
#/cgi-bin/test.py?name=你好&url=http://www.nihao.com

# CGI处理模块
import cgi, cgitb
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

print("Content-type:text/html")
print(      )
print('<html>')
print('<head>')
print('<meta charset=\"utf-8\">')
print('<title> CGI 测试实例！</title>')
print('</head>')
print('<body>')
print('<h2>%s官网：%s</h2>'% (site_name, site_url))
print('</body>')
print('</html>')
