'''CGI编程'''
#CGI是通用网关接口,它是一段程序,运行在服务器上
#在进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序:
#ScriptAlias /cgi-bin/ /var/www/cgi-bin/
#创建一个CGI程序
print("Content-type:text/html")
#" Content-type:text/html"即为HTTP头部的一部分，它会发送给浏览器告诉浏览器文件的内容类
print(          )
# 空行，告诉服务器结束头部
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>Hello World - 我的第一个 CGI 程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello World! 我的第一个CGI程序</h2>')
print('</body>')
print('</html>')

