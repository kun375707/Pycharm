'''CGI环境变量'''
import os

print("Content-type: text/html")
print()
print("<meta charset=\"utf-8\">")
print("<b>环境变量</b><br>");
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print("</ul>")
#这是一个简单的CGI脚本输出CGI的环境变量