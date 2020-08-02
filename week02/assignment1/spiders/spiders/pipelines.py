# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import pandas as pd
import pymysql
class SpidersPipeline:
    def process_item(self, item, spider):
        db = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'Wubab',
                       database = 'mydb',
                       charset = 'utf8mb4'
                        )
        cursor = db.cursor()
        mylist=(item['name'],item['movie_type'],item['time'])
        sql = "INSERT INTO tb1(name,type,time) VALUES ('%s', '%s', '%s')" % mylist
        #print(sql)
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
        return item
