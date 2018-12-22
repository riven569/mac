#!/usr/bin/python
#coding=utf-8
# 0009 找到一个html文件里面的链接
from  urllib.request import urlopen
from bs4 import BeautifulSoup


def find_the_link(path):
    with urlopen(path) as f:
        # print(f)
        text = BeautifulSoup(f,'lxml')

        links= text.find_all('ul')
        for link in links:
            url=link.find_all('a')
            # print(url)
            for l in url:
                l_=l['href']
                print(l_)

find_the_link("https://github.com/Show-Me-the-Code/python/blob/master/Dineshkarthik/0009/0009.py")