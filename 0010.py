# 0010 使用python生成类似于下图中的字母验证码图片
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
import string

def creat_id_code():

    def v_code():
        f_code=''.join(random.choice(string.ascii_uppercase)for i in range(4))
        return(f_code)
    text=v_code()

    def colorRandom():
        return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

    im=Image.new('RGB',(300,200),(255,255,255))
    d=ImageDraw.Draw(im)
    font=ImageFont.truetype('/Macintosh HD/Library/Fonts/Chalkboard.ttc',100)
    for w in range(300):
        for h in range(200):
            d.point((w,h),fill=colorRandom())
    x=20 #自己设置的

    for i in text:
        d.text([x,50],i,colorRandom(),font)
        x+=60 #根据大小调制的

    im=im.filter(ImageFilter.BLUR)
    im.show()
creat_id_code()




#change 噪点频率
# def create_identifying_code(strs,width=400,height=200,chance=2):
#     im= Image.new(IMage_mode,(width,height),Image_BG_color)
#     draw= ImageDraw.Draw(im)
#     for w in xrange(width):
#         for h in xrange(height):
#             if chance < random.randint(1, 100):
#                 draw.point((w, h), fill=colorRandom())
#
#     font=ImageFont.truetype(Image_font,'80')
#     font_width,font_height = font.getsize(strs)
#     strs_len=len(strs)
#     x=(width - font_width)/2
#     y=(height-font_height)/2
#
#     for i in strs:
#         draw.text((x,y),i,colorRandom(),font)
#         x+=font_width/strs_len
#     im=im.filter(ImageFilter,BLUR)
#     im.save('identifying_code_pic.jpg')
# create_identifying_code(text)








