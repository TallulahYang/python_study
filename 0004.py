#! /usr/bin/env python3
# coding: utf-8

# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
import os
from PIL import Image

pathDir='images/0004/'
os.chdir(pathDir)

def modify_imgsize():

    for filename in get_imglist():
        img=Image.open(filename)
        if max(img.size)>1136:
            value=max(img.size)/1136.0
            newsize_min=min(img.size)/value
            newimg = img.resize((1136,int(newsize_min)),Image.ANTIALIAS) #修改大小
            newimg.save('new_'+filename)
        else:
            print("This picture is availabe:"+filename)

def get_imglist(): #获取照片名称list
    img_list=[]
    list_dir=os.listdir(os.getcwd())
    for x in list_dir:
        # print(x)
        if '.png' in x:
            print(x)
            img_list.append(x)
        elif '.jpg' in x:
            print(x)
            img_list.append(x)
        else:
            print("This is not a picture: "+x)
    return img_list

modify_imgsize()

