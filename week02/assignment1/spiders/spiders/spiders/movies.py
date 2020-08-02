import scrapy
from bs4 import BeautifulSoup as bs
from spiders.items import SpidersItem
from collections import defaultdict
from scrapy.selector import Selector
class MoviesSpider(scrapy.Spider):


    # name = 'httpbin'
    # allowed_domains = ['httpbin.org']
    # # 通过ip查看请求的ip地址
    # start_urls = ['http://httpbin.org/ip']
    # # 通过header 查看user-agent
    # # start_urls = ['http://httpbin.org/headers']

    # def parse(self, response):
    #     print(response.text)

    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #      pass
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        select = Selector(response=response)
        #print(select)
        movies=select.xpath('//div[@class="movie-hover-info"]')
        for movie in movies[:10]:
            item=SpidersItem()
            name = movie.xpath('./div/@title')[0]
            movietype=movie.xpath('./div/text()')[4]
            time=movie.xpath('./div/text()')[-1]
            item['name']=name.extract()
            item['movie_type']=movietype.extract().strip()
            item['time']=time.extract().strip()
            print(name.extract(),movietype.extract().strip(),movie.xpath('./div/text()')[-1].extract())
            yield item


