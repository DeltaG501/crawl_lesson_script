import pymysql

# 检查MYSQL版本信息
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print("Database version:", data)

# 创建database：spiders
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4 ")

# 创建表 students
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
# cursor.execute(sql)
# db.close()

# 向表 students 插入数据
# id = '20120001'
# user = 'Bob'
# age = 20
#
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students (id, name, age) values (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 更新数据
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 删除数据
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# table = 'students'
# condition = 'age>20'
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 查询数据
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >=20 '
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one=cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')