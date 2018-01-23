'''另一个的CGI脚本'''
import cgi
#导入Python的CGI模块来访问表单数据，这也是标准库中的一个模块
import cgitb
cgitb.enable()
#Python的标准库提供了一个CGI跟踪模块(名为cgitb)。启用这个模块时，会在Web浏览器上显示详细的错误信息。
# 这些信息可以帮助你找出CGI哪里出了问题。改正错误并且CGI正常工作后，在关闭CGI跟踪。
import athletemodel
import yate
athletes = athletemodel.get_from_store()
#调用athletemodel中的方法，获取pickle中的数据
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
#访问你所选的数据，得到表单数据
#再得到表单数据中的单选按钮数据'which_athlete'
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athlete_name + ", DOB: " +
                      athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))
#生成所需的HTML页面
print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete": "generate_list.py"}))
#两个链接