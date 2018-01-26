'''控制Web应用'''
#需将应用放在一个特定的文件夹结构中:一个主文件夹(存放代码和配置文件)
#子文件夹一(存放静态内容) 子文件夹二(将HTML模版放在这里)
#下面是一些'样板'码,所有GAE web应用最前面都要有这些代码:
from google.appengine.ext import webapp
#导入App Engine的'Webapp'类
from google.appengine.ext.webapp.util import run_wsgi_app
#导入工具来运行Web应用
class IndexPage(webapp.RequestHandler):
    def get(self):
        pass
app = webapp.WSGIApplication([('/,*',IndexPage)],debug=true)
#创建一个新的'webapp'对象
def main():
    run_wsgi_app(app)
if __name__ == '__main__':
    main()