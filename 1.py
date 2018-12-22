
#对于任何一个文档，统计其中的单词的个数
import re
def get_word_frequencies(file_name):
    dic={}
    txt=open(file_name,'r').read().splitlines()

    n=0
    for line in txt:
        #print (line)
        line = re.sub(r'[.?!,""/]', ' ', line)
        for word in line.split():
            print (word)
            dic.setdefault(word.lower(), 0)
            dic[word.lower()] += 1

        print (dic)






get_word_frequencies('/Users/liujian/Pictures/text/new.txt')



