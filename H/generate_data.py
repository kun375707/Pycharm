'''此脚本为选手数据脚本'''
import cgi
import yate
import json
import athletemodel

athletes = athletemodel.get_from_store()
#从模块中得到所有数据
form_data = cgi.FieldStorage()
athlete_name = form_data['athlete'].value
#处理请求发送的数据
printyate.start_response('application/json')
printjson.dumps(athletes[athlete_name].to_dict())
