# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        mylist=[[item['name'],item['movietype'],item['time']]]
        movie1 = pd.DataFrame(data = mylist)
        movie1.to_csv('./movie1.csv',mode='a+', encoding='utf8', index=False, header=False)
        return item
