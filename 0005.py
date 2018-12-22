'''
It can resize the photos in a file
#coding=utf-8
'''

import os
from PIL import Image

def resize_photo(source_dir,width,height,destination_dir):
    photos = os.listdir(source_dir)
    photos = photos[1:]

    for photo in photos:
        photo_abspath = os.path.join(source_dir,photo)

        print (photo_abspath)


        if (os.path.isfile(photo_abspath)):
            im = Image.open(photo_abspath)
            new_im = im.resize((width,height))

            destination_path = os.path.join(destination_dir, photo)
            new_im.save(destination_path)
            print(destination_path)


resize_photo('/Users/liujian/Pictures/1',900,800,'/Users/liujian/Pictures/2')