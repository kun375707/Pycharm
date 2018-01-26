'''提供选择来限制输入'''
from goole.appengine.ext import db
class Sighting(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()
    date = db.DateProperty()
    time = db.TimeProperty()
    _FINS = ['A','B','C','D']
    _WHALES = ['A','B','C','D']
    _BLOWS = ['A','B','C','D']
    _WAVES = ['A','B','C','D']
    #定义值列表
    location = db.StringProperty(multiline=True)
    #允许多行输入
    fin_type = db.StringProperty(choices=_FINS)
    whale_type = db.StringProperty(choices=_WHALES)
    blow_type = db.StringProperty(choices=_BLOWS)
    wave_type = db.StringProperty(choices=_WAVES)
    #使用值列表