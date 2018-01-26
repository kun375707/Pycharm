'''将代码整合'''
from google.appengine.ext import webapp
#导入App Engine的'Webapp'类
from google.appengine.ext.webapp.util import run_wsgi_app
from goole.appengine.ext import db
from google.appengine.ext.webapp import template
from goole.appengine.ext.db import djangoforms
import hfwwgDB
#导入GAE数据模块代码
class SightingForm(djangoforms.ModelForm):
    #使用模型创建一个表单
    class Meta:
        model = hfwwgDB.Sighting
        #继承'django.ModelForm'类
class SigthingInputPage(webapp.RequestHandler):
    #连接处理器类名,它提供了 get 的方法来响应请求
    def get(self):
        html = template.render('templates/header.html', {'title': 'Report a Possible Sighting'})
        html = html + template.render('templates/form_start.html', {})
        html = html + str(SightingForm())
        html = html + template.render('templates/form_start.html', {'sub_title': 'Submit Sighting'})
        html = html + template.render('templates/form_start.html', {'link': ''})
        self.response.out.write(html)
app = webapp.WSGIApplication([('/,*',SigthingInputPage)],debug=true)
def main():
    run_wsgi_app(app)
if __name__ == '__main__':
    main()