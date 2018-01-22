'''第三步 控制你的代码'''
#主要是合理安排WEB应用的目录结构
#首先是 项目文件夹(名字随意）其中还包含3个子文件夹，index.html文件,'favicon.ico'图标等
#子文件有：'cgi-bin'(为web应用写的所有代码需放入其中,就是CGI脚本)
#'data'文件夹是存放数据文件,比如TXT文件都在这里
#'templates'文件夹可以存放HTML页面的模版代码,例如Yate模版

from http.server import HTTPServer, CGIHTTPRequestHandler
#导入HTTP服务器和CGI模块
port = 8080
#指定一个端口
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
#创建一个HTTP服务器
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
#显示一个友好的信息，并启动服务器
#用Python构建一个Web服务器必须有以上5行代码。