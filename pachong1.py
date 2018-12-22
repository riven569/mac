#!/usr/bin/python
#coding=utf-8
# python中的爬虫的练习
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    'https://morvanzhou.github.io/static/scraping/list.html'
).read().decode('utf-8')
#print(html)

"""res = re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)
print('\nPage paragraph is :',res[0])
"""

soup= BeautifulSoup(html,'lxml')
month = soup.find_all('li',{'class':'month'})
for m in month:
    print(m.get_text())
jan = soup.find('ul',{'class':'jan'})
d_jan = jan.find_all('li')
for n in d_jan:
    print(n.get_text())




