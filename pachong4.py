#使用requests来baidu搜索
# import requests
# param= {"wd":"puhunba"}
# r= requests.get('http://www.baidu.com/s',params=param)
# print(r.url)

import requests
import os
os.makedirs('./Pictures',exist_ok=True)

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

r= requests.get(IMAGE_URL,stream=True)
with open('./Pictures/image3.png','wb')as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)


