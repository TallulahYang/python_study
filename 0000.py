#! /usr/bin/env python
# coding: utf-8

# 图片右上角加上红色的数字

__author__ = 'Tallulah Yang'

from PIL import Image,ImageDraw,ImageFont
import random
im = Image.open('7910463.jpg')

msgNum = str(random.randint(1,99))

d = ImageDraw.Draw(im)
d.rectangle((20,20,50,50),outline = "red")
d.text([10,10],msgNum,"red")

del d

im.save("7910463-1.jpg")