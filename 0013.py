#!/usr/bin/python
# coding=utf-8

"""
用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 http://tieba.baidu.com/p/2166231880?traceid=)
"""
import requests
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2166231880?traceid='
html = requests.get(url).text
# print (html)
soup = BeautifulSoup(html, 'lxml')
img_cc = soup.find_all('cc')
for cc in img_cc:
    imgs=cc.find_all('img')
    for img in imgs:
        link= img['src']
        r = requests.get(link, stream=True)
        image_name=link.split('/')[-1]
        with open('./Pictures/%s'%image_name,'wb')as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('saved as %s'%image_name)