#!/usr/bin/python
# coding=utf-8

"""
第 0015 题： 纯文本文件 city.txt为城市信息,
里面的内容（包括花括号）如下所示：：

"""
import os,json,xlwt

def read_text():
    with open('./city.txt','r')as f:
        text=f.read()
        text_json=json.loads(text)
        return (text_json)
def save_to_excel(content_dict,excel_name):
    wb= xlwt.Workbook()
    ws= wb.add_sheet('city',cell_overwrite_ok=True)
    row=0
    col=0
    for k,v in sorted(content_dict.items(),key=lambda d:d[0]):
        print(content_dict)
        ws.write(row,col,k)
        ws.write(row,col+1,v)
        row+=1
        col=0
    wb.save(excel_name)

if __name__ == "__main__":
    save_to_excel(read_text(),'city.xls')