#!/usr/bin/python
#coding=utf-8
# python中的爬虫的练习 爬百度百科
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

base_url = "https://baike.baidu.com"
history = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"]
url = base_url + history[-1]



for i in range(100):
    url=base_url + history[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    print (soup.find('h1').get_text(),' url:', history[-1])
    sub_urls = soup.find_all("a",{"target":"_blank" , 'href': re.compile("/item/(%.{2})+$")})


    if len(sub_urls)!=0:
        history.append(random.sample(sub_urls,1)[0]['href'])
    else:
        history.pop()
    print (history)