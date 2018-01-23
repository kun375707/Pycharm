'''此脚本获取Json数据'''
import yate
import athletemodel
import json
import cgitb

cgitb.enable()

names = athletemodel.get_names_from_store()

printyate.start_response('application/json')
json.dumps(sorted(names))