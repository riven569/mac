#!/usr/bin/python
#coding=utf-8
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def find_the_content(path):
    with urlopen(path) as f:
        print(f)
        text = BeautifulSoup(f,'lxml')
        content = text.get_text()
       # for line in content:
        for line in content.splitlines():
            if re.search('\S',line):
                print(line)

find_the_content("https://github.com/Show-Me-the-Code/python/blob/master/Jaccorot/0008/Show-Me-the-Code_show-me-the-code_1.html")