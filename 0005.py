#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
统计出你认为每篇日记最重要的词
"""

import os

def count_words(inputname):
    fh=open(inputname)
    read_fh=fh.read()
    fh.close()
    number=1
    is_alpha=[]
    dict_words={}
    ignore_words=['a','an','is','it','are','of','by','the','and','for','in','to']

    for word in read_fh:#取出文本中的非英文字符
        if word.isalpha():
            is_alpha.append(word)
        elif word=='\t' or word=='\n' or word==' ':
            is_alpha.append(word)

    fh_alpha=''.join(is_alpha)
    fh_words=fh_alpha.split()
    for words in fh_words: #建立单词及频次的字典
        print(words)
        words=words.lower()
        if words not in dict_words and words not in ignore_words:
            dict_words[words]=number
        elif words in ignore_words:
            continue
        else:
            dict_words[words]=dict_words[words]+1

    #字典按值排序
    dict_sort= sorted(dict_words.items(), key=lambda d:d[1], reverse = True)

    print('Maximum number of words is "%s" and it appear "%d" times'%(dict_sort[0][0],dict_sort[0][1]))
    print('Second number of words is "%s" and it appear "%d" times'%(dict_sort[1][0],dict_sort[1][1]))
    print('Third number of words is "%s" and it appear "%d" times'%(dict_sort[2][0],dict_sort[2][1]))

count_words("text.txt")