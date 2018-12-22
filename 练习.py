
from PIL import Image,ImageDraw,ImageFont
import glob,os

#
# im=Image.open('download.jpeg')
# draw= ImageDraw.Draw(im)
# draw.line((0,50)+im.size,fill=1,width=20)
# draw.line
# im.save('download11.jpeg')
# im.show

"""
base=Image.new('RGB',(1024,768),(255,255,255))

# base.save('base.jpeg')
d=ImageDraw.Draw(base)
d.text([0,50],text="hello",fill=(255,2,255))
# d.line([(20,3),(200,300)],fill=1,width=20)
base.show()
"""

"""
1
text='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb' \
     'rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
all_word=''
for i in text:
    # print (i)
    c=ord(i)
    print(c)
    if 96<c<120:
        new=chr(c+2)
    elif c>120:
        new=chr(c-24)
    else:
        new=chr(c)
    all_word+=new
print(all_word)
print(ord('y'))
"""

for i in range(1000):
    
    print(i)
