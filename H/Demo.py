'''利用Python开发移动应用'''
#1.下载开发包SDK
#2.打开SDK Manager,安装所需要的packages
#3.选择Tools-->Manage AVDs，添加一个新的Android虚拟设备（AVD）
#4.打开模拟器设备，点击模拟器的浏览器，导航的下面地址：
# https://code.google.com/p/android-scripting/
#5.下载SL4A包并安装，安装完成后回到浏览器，选择Downloads标签页，下载安装python_form_andorid_rx.apk.
#6.安装完成后打开该软件，点击Install，下载解压安装面向Android的Python支持文件
#7.测试Python脚本,要把脚本传送到模拟器，需要把它复制到模拟器的虚拟SD卡中,
#并输入tools/adb push mydroidtest.py /sdcard/sl4a/scripts命令
'''利用JSON(web上的数据交换格式)传输数据'''
import json
names = ['John',['Johnny','Jack'],'Michael',['Mike','Mikey','Mick']]
#创建一个多重列表
print(names)
to_transfer = json.dumps(names)
#转换为一个Json多重列表
print(names)
fron_transfer = json.loads(to_transfer)
#将Json多重列表换回原来格式
print(names)
