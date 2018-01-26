'''利用模版构建视图'''
#这个试图要为Web应用显示一个数据输入表单
from google.appengine.ext.webapp import template
html = template.render('templates/header.html',{'title':'Report a Possible Sighting'})
html = html + template.render('templates/form_start.html',{})
#render()函数总是需要两个参数，如果不需要第二个需传入一个空字典
html = html + template.render('templates/form_start.html',{'sub_title':'Submit Sighting'})
html = html + template.render('templates/form_start.html',{'link':''})
#借助Django表单生成技术(实例如下):
from goole.appengine.ext.db import djangoforms
import birthDB
class BirthDetailsForm(djangoforms.ModelForm):
    class Meta:
        model = birthDB.BirthDetails

        html = template.render('templates/header.html', {'title': 'Report a Possible Sighting'})
        html = html + template.render('templates/form_start.html', {})
        html = html + str(BirthDetailsForm(auto_id=Flase))
        #用这个新类生成表单
        html = html + template.render('templates/form_start.html', {'sub_title': 'Submit Sighting'})
        html = html + template.render('templates/form_start.html', {'link': ''})
