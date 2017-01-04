#! /usr/bin/env python
# coding: utf-8
__author__ = 'Tallulah Yang'

from PIL import Image,ImageFont,ImageDraw
import sys

args = sys.argv
if len(args)==1:
    imgpath = '7910463.jpg'
elif len(args) == 2:
    imgpath = args[1]
else:
    print('Too many arguments!')

#print(imgpath)
ascii_char = list("$@&%B#=-. ")

#print(ascii_char)

def select_ascii_char(r, g, b):
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)  # ‘RGB－灰度值’转换公式
    unit = 256.0/len(ascii_char)  # ascii_char中的一个字符所能表示的灰度值区间
    return ascii_char[int(gray/unit)]


def output(imgpath, width=100, height=100):
    im = Image.open(imgpath)
    im = im.resize((width, height), Image.NEAREST)

    txt = ""

    for h in range(height):
        for w in range(width):
            txt += select_ascii_char(*im.getpixel((w, h))[:3])  # [:3] 切片  * 表示为可变参数
        txt += '\n'
    return txt

def save_as_txtfile(txt):
    with open('imgtochar.txt', 'w') as f:
        f.write(txt)
        f.close()

if __name__ == '__main__':
    txt = output(imgpath, 120, 120)
    print(txt)
    save_as_txtfile(txt)

    font = ImageFont.truetype('Arial.ttf', 18)
    im = Image.new("RGB", (1200, 1200), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    dr.text((0,0),txt,fill="#000000")
    im.save("1.1.jpg")