import requests
from bs4 import BeautifulSoup as bs
from collections import defaultdict
import pandas as pd
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookies = r'_lxsdk_cuid:1738a51c20dc8-01ba7785c521b3-4c302372-144000-1738a51c20dc8;_lxsdk:2BAD7290CF1D11EABDA91DE1C2FF6305D5664C25727D4750A4D84F438DE8C9D8;Hm_lvt_703e94591e87be68cc8da0da7cbd0be2:1595753479;Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2:1595753883;_lxsdk_s:1738a51c20e-f8f-41d-6f1%7C%7C21;__mta:19239431.1595753480843.1595753630241.1595753883701.11'

cookies_dict={}#初始化cookies字典变量
for line in cookies.split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split(':',1)
    cookies_dict[name]=value 
headers = {'Accept': '*/*',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive'
           }

myurl='https://maoyan.com/films?showType=3'

response=requests.get(myurl,headers=headers,cookies=cookies_dict)

bs_info = bs(response.text, 'html.parser')
moviedict=defaultdict(dict)
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
    for atag in tags.find_all('div',attrs={'class':'movie-hover-title'}):
        name=atag.get('title')
        hovertag=atag.find('span')
        if hovertag:
            tagtype=hovertag.text.strip()
            if tagtype in ['上映时间:','类型:']:
                txt=atag.text.strip().split('\n')[1].strip()
                moviedict[name][tagtype]=txt
        # 获取电影名字


print('返回码是: ',response.status_code)
mylist=[]
for movie in moviedict:
    mylist.append([movie,moviedict[movie]['上映时间:'],moviedict[movie]['类型:']])

movie1 = pd.DataFrame(data = mylist)

movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

