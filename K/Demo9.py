'''准备Android应用的代码'''
import time
import android
#完成导入
distances = [ '2mi', '5k', '5mi', '10k', '15k', '10mi', '20k',
                '13.1mi', '25k', '30k', 'Marathon' ]
#创建一个行标签列表
hello_msg = "Welcome to the Marathon Club's App"
quit_msg = "Quitting the Marathon Club's App."
#定义两个友好信息
app = android.Android()
#创建android应用对象，并包含你的辅助函数
def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)
