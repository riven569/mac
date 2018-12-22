#!/usr/bin/python
#coding=utf-8
# python中的爬虫的练习
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen(
    'https://morvanzhou.github.io/static/scraping/table.html'
).read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')

# img_links = soup.find_all("img",{'src': re.compile('.*?\.jpg')})
# for link in img_links:
#     print (link['src'])

course_links = soup.find_all('a',{'href': re.compile('https://morvan.*')})
# print (course_links)
for linkin in course_links:
    print(linkin['href'].lower())
