import pymysql

db= pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'Wubaba950823',
                       database = 'mydb',
                       charset = 'utf8mb4'
                        )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句  里面的数据类型要对应
sql = "INSERT INTO tb1(name,type,time) VALUES ('%s', '%s', '%s')" % ('test3','经典','2019/12/14')
print(sql)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 执行sql语句
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
