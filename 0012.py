
#!/usr/bin/python
# coding=utf-8

"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
def tran_to_star():

    with open('filtered_words.txt','r') as f:
        text= f.read()
        text=text.splitlines()
        # print (text)

    # judge_flag=False
    type_in = input('请输入：\n')
        # print(i)
    for i in text:
        if i in type_in:
            type_in=type_in.replace(i,'**')

    # if judge_flag:
    #     print('freedom')
    # else:
    #     print("Human rights")
    print(type_in)
tran_to_star()
