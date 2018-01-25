'''将新数据库与Web应用集成'''
#从数据库得到名字:
import sqlite3
db_name = 'coachdata.sqlite'
def get_names_from_store():
    connection = sqlite3.connect(db_name)
    #连接到数据库
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name FROM athletes""")
    #抽取数据
    response = [row[0] for row in results.fetchall()]
    #建立一个响应
    connection.close()
    return(response)
    #向调用者返回名字列表

#得到选手名和ID值
def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)

#根据ID得到选手的详细信息
def get_athlete_from_id(athlete_id):
    #这是新函数，获取与指定ID关联的数据
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""", (athlete_id,))
    (name, dob) = results.fetchone()
    #从athletes表获取 name 和 dob
    results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""", (athlete_id,))
    data = [row[0] for row in results.fetchall()]
    #得到时间列表
    response = {'Name':   name,
                'DOB':    dob,
                'data':   data,
                'top3':   data[0:3]}
    #转换为一个字典
    connection.close()
    return(response)
#最后修改generate的四个CGI脚本，将SQLite数据库移至web应用的顶层目录中