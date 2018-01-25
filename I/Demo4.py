'''使用数据管理系统'''
#Python3预装了SQLite3，这是一个完备的，无需设置的基于sql的数据管理系统,可以把数据放入SOLite中。
#要使用SQLite，只需导入sqlite3库，并使用Python的标准化数据库API来编程。
#如下为使用splite3模块实现与数据库的一个交互:
import sqlite3
connettion=sqlite3.connect('test.sqiite')
#建立连接
cursor=connection.crusor()
#创建数据游标
cursor.execute("""SELECT DATE('NOW')""")
#执行一些SQL操作
connection.commit()
#提交做出的修改
connection.close()
#定义数据库模式
#利用如下程序创建数据库名为coachdata.sqlite，他有两个表，一个athletes，包含一个ID值，选手名和出生日期，
# 一个timing_data，包含选手的唯一ID和具体的时间值。
import os
import sqlite3

connection = sqlite3.connect('coachdata.sqlite')

cursor = connection.cursor()
cursor.execute("""CREATE TABLE athletes (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,name TEXT NOT NULL,dob DATE NOT NULL )""")
cursor.execute("""CREATE TABLE timing_data (athlete_id INTEGER NOT NULL,value TEXT NOT NULL,FOREIGN KEY (athlete_id) REFERENCES athletes)""")

connection.commit()
connection.close()