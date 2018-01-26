'''用Google App Engine构建web应用(以表单为例)'''
#1.安装APP Engine和Python2.5
#2.测试GAE,创建名为mygaetest的文件夹(包含一个测试脚本和一个名为app.yaml的配置文件)
#3.让APP Engine使用MVC模式 （包括对数据建模 利用模版构建视图 控制器）
#数据建模:
from goole.appengine.ext import db
class Sighting(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()
    date = db.DateProperty()
    time = db.TimeProperty()
    location = db.StringProperty()
    fin_type = db.StringProperty()
    whale_type = db.StringProperty()
    blow_type = db.StringProperty()
    wave_type = db.StringProperty()
#分配属性类型
