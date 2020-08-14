import pymysql
import pandas as pd
db= pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'Wubaba950823',
                       database = 'mydb',
                       charset = 'utf8mb4'
                        ) 
sql='SELECT * FROM tb1'
data=pd.read_sql(sql,db)                       
#SELECT * FROM data;
data
# SELECT * FROM data LIMIT 10;
data[:10]
#SELECT id FROM data;  //id 是 data 表的特定一列
data['id']
# SELECT COUNT(id) FROM data;
data['id'].count()
#SELECT * FROM data WHERE id<1000 AND age>30;
data[(data['id']<1000) & (data['age']>30)]
#SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
data.groupby('id').agg({'order_id':'nunique'})
#SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(t1,t2,on='id')
#SELECT * FROM table1 UNION SELECT * FROM table2;
pd.merge(table1,table2,how='outer')
#DELETE FROM table1 WHERE id=10;
table1=table1.drop(table1[table1['id']==10].index)
#ALTER TABLE table1 DROP COLUMN column_name;
table1=table1.drop(['column_name'],axis=1)
