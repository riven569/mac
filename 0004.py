#coding=utf-8
#对于任何一个文档，统计其中的单词的个数


import re
def get_frequence (file_name):
    dict={}
    txt = open(file_name ,'r').read().splitlines()
    n=0
    for line in txt:
        line=re.sub(r'[#,.?/\'\"]','',line)
        for word in line.split():
            dict.setdefault(word.lower(),0)
            dict[word.lower()]+=1
            print (word)
            n+=1

    print (dict)
    print (n)
get_frequence('dog')