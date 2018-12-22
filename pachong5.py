# 爬国家地理的图片

import requests
import os
from bs4 import BeautifulSoup
URL='http://www.ngchina.com.cn/animals/'
html= requests.get(URL).text
soup= BeautifulSoup(html,'lxml')
img_ul = soup.find_all('ul',{'class':'img_list'})
# print(img_ul)
for ul in img_ul:
    imgs= ul.find_all('img')
    for img in imgs:
        url=img['src']
        r=requests.get(url,stream=True)
        image_name=url.split('/')[-1]
        with open('./Pictures/%s' %image_name,'wb')as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
            print('saved %s'%image_name)
