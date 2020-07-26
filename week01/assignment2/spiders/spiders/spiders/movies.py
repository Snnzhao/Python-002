import scrapy
from bs4 import BeautifulSoup as bs
from spiders.items import SpidersItem
from collections import defaultdict
from scrapy.selector import Selector
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):

        # bs_info = bs(response.text, 'html.parser')
        # moviedict=defaultdict(dict)
        # for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
        #     for atag in tags.find_all('div',attrs={'class':'movie-hover-title'}):
        #         name=atag.get('title')
        #         hovertag=atag.find('span')
        #         if hovertag:
        #             tagtype=hovertag.text.strip()
        #             if tagtype in ['上映时间:','类型:']:
        #                 txt=atag.text.strip().split('\n')[1].strip()
        #                 moviedict[name][tagtype]=txt
        # for name in moviedict:
        #     item=SpidersItem()
        #     item['name']=name
        #     item['movietype']=moviedict[name]['类型:']
        #     item['time']=moviedict[name]['上映时间:']
        #     #items.append(item)
        #     #print(name,moviedict[name]['类型:'],moviedict[name]['上映时间:'])
        #     yield item
        select = Selector(response=response)
        movies=select.xpath('//div[@class="movie-hover-info"]')
        for movie in movies[:10]:
            item=SpidersItem()
            name = movie.xpath('./div/@title')[0]
            movietype=movie.xpath('./div/text()')[4]
            time=movie.xpath('./div/text()')[-1]
            item['name']=name.extract()
            item['movietype']=movietype.extract().strip()
            item['time']=time.extract().strip()
            #print(name.extract(),movietype.extract().strip(),movie.xpath('./div/text()')[-1].extract())
            yield item

