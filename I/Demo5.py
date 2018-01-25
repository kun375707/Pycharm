'''从pickle向SQLite传输数据'''
#除了创建表，还要将数据传到数据库模型中
import sqlite3
connection = splite3.connect('coachdata.sqlite')
#L连接到新数据库
cursor = connection.cursor()
import glob
import athletemodel
data_files = glob._glob0('../data/.txt')
#从现有模版获取数据
athletes = athletemodel.put_to_store(data_files)
for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    #从腌制数据得到名字和出生日期
cursor.execute('INSERT INTO athletes(name,dob) VALUES(?,?))',(name.dob))
#使用INSERT语句向athletes表增加新数据行
connection.commit()

#如何在Pyhton中使用SELECT语句：
cursor.execute("SELECT id from athletes WHERE name=? AND dob=?",(name,dob))
#?占位符允许为SQL语句指定参数
#查询数据库
cursor.fetchone()# 返回下一个数据行
cursor.fetchmany()# 返回多个数据行
cursor.fetchall()# 返回所有数据行
#可以在游标上调用多个不同方法来访问结果


cursor.execute("SELECT id from athletes WHERE name=? AND dob=?", (name, dob))
the_current_id = cursor.fetchone()[0]
#查询athletes表，得到选手的名字和出生日期，将结果赋至变量the_current_id。
for each_time in athletes[each_ath].clean_data:
    cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)",
                       (the_current_id, each_time))
# 再写一个查询从pickle中抽取选手的时间，把它们增加到timing_data表。
connection.close()
