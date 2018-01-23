'''显示选手列表的脚本'''
#Web服务器执行这个程序时，会动态生成一个HTMLWeb页面。目标是建立一个CGI脚本，从而生成目标HTML页面。
import glob
#利用glob模块可以想操作系统查询一个文件名列表
import athletemodel
#导入之前创建的athletemodel
import yate
data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
print(yate.start_response())
#总是从一个Content_type行开始
print(yate.include_header("Coach Kelly's List of Athletes"))
#开始生成web页面，提供一个合适的标题
print(yate.start_form("generate_timing_data.py"))
#开始生成表单，提供要链接的服务器端程序的名。
print(yate.para("Select an athlete from the list to work with:"))
#一行文字
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
#为各个选手分别生成一个单选钮
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
#创建一个提交按钮