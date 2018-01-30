'''增加对话框'''
#假设一个名为distances的列表，其中包含行距标签(2mi,5k,5mi等)
#提供两个必要的do_dialog()函数来创建Demo7的显示:
do_dialog("Pick a distance", distances,
          #提供对话框标题和要显示的项列表
          app.dialogSetSingleChoiceItems)
#提供要使用的对话框类型
do_dialog("Pick a distance to predict", distances,
          app.dialogSetSingleChoiceItems)
#同上
do_dialog('The predicted time running ' + predicted_distance +
#根据变量来创建对话框标题
          ' is: ',prediction, app.dialogSetItems, "OK", None)
#覆盖对话框按钮的缺省值