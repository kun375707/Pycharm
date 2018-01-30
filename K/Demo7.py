'''工具函数'''
#这个应用通过一系列对话框与用户交互,创建一个工具函数抽象出对话框创建细节
def do_dialog(title, data, func, ok='Select', notok='Quit'):
    #参数分别为对话框的标题,显示的值列表，对话框创建方法名，按钮的文本(有缺省值)
    app.dialogCreateAlert(title)
    func(data)
    app.dialogSetPositiveButtonText(ok)
    if notok:
        app.dialogSetNegativeButtonText(notok)
    app.dialogShow()
    return(app.dialogGetResponse().result)
#显示对话框然后返回所选择的项