#!/usr/bin/python
# coding=utf-8

"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

"""
import os,json,xlwt

def read_text():
    with open('./numbers.txt','r')as f:
        text=f.read()
        text_json=json.loads(text)
        return (text_json)
def save_to_excel(content_dict,excel_name):
    wb= xlwt.Workbook()
    ws= wb.add_sheet('numbers',cell_overwrite_ok=True)
    row=0
    col=0
    # for k,v in sorted(content_dict.items(),key=lambda d:d[0]):
    for i in content_dict:
        # print(content_dict)
        # ws.write(row,col,i[0])
        for n in i:
            ws.write(row,col,n)
            col+=1
        row+=1
        col=0
    wb.save(excel_name)

if __name__ == "__main__":
    save_to_excel(read_text(),'numbers.xls')