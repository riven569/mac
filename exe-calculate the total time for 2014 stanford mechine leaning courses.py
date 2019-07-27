#coding=utf-8


from os import listdir
import re


total_time = 0
my_path = '/Users/liujian/Courses/2014 Meachine Learning Stanford'

for f in listdir(my_path):
    the_digit = ''.join(re.findall('\(\d+\s',f)).strip('(')
    if the_digit == '':
        pass
    else:
        print(int(the_digit))
        total_time += int(the_digit)
print(total_time)













