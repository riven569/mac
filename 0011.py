#!/usr/bin/python
# coding=utf-8

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights。
"""

def tran_to_words():

    with open('filtered_words.txt','r') as f:
        text= f.read()
        text=text.splitlines()
        # print (text)

    judge_flag=False
    type_in = input('请输入：\n')
        # print(i)
    # for i in text:
    if type_in in text:
        judge_flag = True

    if judge_flag:
        print('freedom')
    else:
        print("Human rights")

tran_to_words()