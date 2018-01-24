'''使用表单或对话框接收输入'''
#在web上，用户可以与web表单交互并输入数据。
# 在android手机上，可以使用dialogGetInput()方法得到用户的输入，然后通过代码模拟web表单按钮的行为。
#创建一个HTML表单模版步骤：
#1.首先创建一个新模板名为form.html 2.为该模版增加两个函数 create_inputs() 和 do_form() 3.利用脚本test-form.py可生成表单

from string import Template
#从标准库的"string"模块导入"Template"类，它支持简单的字符串替换模板
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')
#这个函数需要一个字符串作为参数，用它来创建一个"Content-type"
#参数缺省值是"text/html"

def include_header(the_title):
    with open('templates/header.html') as headf:
        # 打开模板文件(HTML),读入文件
        head_text = headf.read()
    header = Template(head_text)
    #换入所提供的标题
    return(header.substitute(title=the_title))
#这个函数需要一个字符串作为参数，用在HTML页面最前面的标题中
#页面本身存储在一个单独的文件"templates/header.html"中，可以按需替换标题
#read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    #换入所体统的HTML链接字典
    return(footer.substitute(links=link_string))
#与"include_header"函数类似，这个函数使用一个字符串作为参数，来创建一个HTML页面尾部
#页面本身存储在一个单独的文件'templates/footer.html'中，参数用于动态地创建一组HTML链接标记
#参数应当是一个字典

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')
#这个函数返回表单最前面的HTML，允许调用者制定URL(表单数据将发送到这个URL)
#还可以制定要使用的方法（POST或GET）

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
#这个函数返回表单末尾的HTML标记，同时还允许调用者定制表单"submit"按钮的文本

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')
#这个函数给定一个单选按钮名和值，创建一个HTML单选钮(通常包括在一个HTML表单中)

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)
#给定一个项列表，这个函数会把该列表转换为一个HTML无序列表
#for循环就可以完成全部工作，每次迭代会想ul元素添加一个li元素

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')
#创建并返回一个HTML标题标记（H1等），默认为H2，header_text参数是必须的
#header()函数允许快速建立选定级别的HTML标题(默认为2）

def para(para_text):
    return('<p>' + para_text + '</p>')
#para()函数会把一个文本块包围在HTML段落标记中间:<p>...</p>

def create_inputs(inputs_list):
    html_inputs = ''
    for each_input in inputs_list:
        #分别创建一个<input>标记
        html_inputs = html_inputs + '<input type="Text" name="' + each_input + '" size=40>'
    return(html_inputs)

def do_form(name, the_inputs, method="POST", text="Submit"):
    with open('I/form.html') as formf:
        #从硬盘中获得模版
        form_text = formf.read()
    inputs = create_inputs(the_inputs)
    #创建<input>列表
    form = Template(form_text)
    #创建一个模版表单
    return(form.substitute(cgi_name=name,http_method=method,list_of_inputs=inputs,submit_text=text))