#coding=utf-8

from PIL import Image, ImageDraw,ImageFont
import random

msgNum = str(random.randint(1,99))

# Read image
im = Image.open('download.jpeg')
w,h = im.size
wDraw = 0.8 * w
hDraw = 0.08 * w

# Draw image
font = ImageFont.truetype('/Macintosh HD/System/Library/Fonts/Symbol.ttf',36)
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), msgNum, font=font, fill = (255,33,33))

#save image
im.save(('ljlx_msg.jpeg'),'jpeg')

