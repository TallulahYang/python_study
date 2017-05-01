#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
图片清晰化
"""

from PIL import Image,ImageFilter,ImageDraw,ImageEnhance,ImageOps
import sys
import random

# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('images/0/WechatIMG3.png')
# im = Image.open('7910463.jpg')

# im = im.filter(ImageFilter.EDGE_ENHANCE)
# im = im.convert('1')

brightness = ImageEnhance.Brightness(im)#获取亮度增强对象
bright_img = brightness.enhance(2.0)#亮度增加两倍
# bright_img.save("bright.jpg")#保存

sharpness = ImageEnhance.Sharpness(im)#获取图片尖锐化对象
sharp_img = sharpness.enhance(7.0)#尖锐化
# sharp_img.save("sharpness.jpg")#保存

contrast = ImageEnhance.Contrast(im)#获取对比度对象
contrast_img = contrast.enhance(2.0)#增加对比度
# contrast_img.save("contrast.jpg")

def processImage(im):
    im = im.convert("L")

    im = ImageEnhance.Brightness(im)
    im = im.enhance(2.0)
    im = ImageEnhance.Contrast(im)
    im = im.enhance(2.0)
    im = ImageEnhance.Sharpness(im)
    im = im.enhance(5.0)

    im = ImageOps.invert(im)
    return im

im = processImage(im)
im.save('result1.png')

# # 获得图像尺寸:
# w, h = im.size
#
# print(w,h)
#
# for h in range(h):
#     for w in range(w):
#         # print(*im.getpixel((w, h))[:3])
#         print(im.getpixel((w, h)))

# 缩放到50%:
# im.thumbnail((w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('WechatMG3thumbnail.png', 'png')


#
# im2 = Image.open('images/0/WechatIMG3.png')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('WechatMG3thumbnail2.png', 'png')




