'''存储数据'''
#若要处理提交数据要增加一个名为post()的方法
#之后代码将存储在GAEdatastore中:
def post(self):
    new_sighting = hfwwgDB.Sighting()
    #创建一个新的'sighting'对象
    new_sighting.name = self.request.get('name')
    new_sighting.email = self.request.get('email')
    new_sighting.date = self.request.get('date')
    new_sighting.time = self.request.get('time')
    new_sighting.location = self.request.get('location')
    new_sighting.fin_type = self.request.get('fin_type')
    new_sighting.whale_type = self.request.get('whale_type')
    new_sighting.blow_type = self.request.get('blow_type')
    new_sighting.wave_type = self.request.get('wave_type')
    new_sighting.which_user = user.get_current_user()
    #对于从HTML表单接收的各个数据值,将它们分别赋至新创建的对象的属性
    new_sighting.put()
    #将已填充数据的对象存储在GAE datastore中
    html = template.render('templates/header.html', {'title': 'Thank you!'})
    html = html + '<p>Thank you for providing your sigthing data.</p>'
    html = html + template.render('templates/form_start.html', {'link': 'Enter<a href="/">another sighting</a>.'})
    self.response.out.write(html)
    #将响应发送到正在等待的Web浏览器



