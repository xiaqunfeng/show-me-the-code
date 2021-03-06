#!/usr/bin/env python #coding=utf-8

from PIL import Image, ImageDraw, ImageFont

def img_addnum(img_name, num):
    im = Image.open(img_name)
    draw = ImageDraw.Draw(im)

    #width and height
    w = im.width;
    h = im.height;
    #anotheer method
    #w, h = im.size
    #print(h, w)
    
    #load font
    fnt = ImageFont.truetype('Arial.ttf', int(h * 0.15))

    draw.text((w * 0.9 , h * 0.05), num, font=fnt, fill=(255, 0, 0, 128))
    im.save(img_name.split('.')[0] + '2.jpg')

if __name__ == '__main__':
    img_addnum('cat.jpg', '3')
