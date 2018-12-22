#coding=utf-8

#200个验证码

import random,string

#for i in range (100)
Letter = string.ascii_uppercase + string.digits

def lj_code():
    letter = ''.join((random.choice(Letter))for k in range (10))
    print(letter)


for i in range(200):
    lj_code()