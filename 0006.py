"""
**第 0006 题：**
你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import os
import re
def find_word(dirPath):
    if not os.path.isdir(dirPath):
        return
    fileList = os.listdir(dirPath)
    fileList=fileList[1:]
    #print (fileList)

    reObj = re.compile('\b?(\w+)\b?')
    for file in fileList:
        filePath = os.path.join(dirPath,file)
        #print(filePath)

        with open(filePath) as f:
            data =f.read()
            words= reObj.findall(data)
            Dic = dict()

            for word in words:

                word = word.lower()
                #print(word)

                if word in ['a','the','to','of','and','in']:
                   continue
                if word in Dic:
                    Dic[word]+=1
                else:
                    Dic[word]=1

        finalList = sorted(Dic.items(),key=lambda item:item[1], reverse=True)
        #print (finalList)
        print('file:%s  and the most word is %s'%(file,finalList[0]))

find_word('/Users/liujian/Pictures/text')