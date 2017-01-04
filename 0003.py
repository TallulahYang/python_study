#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re


def count_words(file_path):
    with open(file_path) as file:
        text = file.read()
        words = re.findall(r'[a-zA-Z]+', text)
        count = len(words)
    return count

print(count_words('text.txt'))




import collections

with open('text.txt') as file1:
    str1=file1.read().split(' ')

print("原文本:\n %s"% str1)
print("\n各单词出现的次数：\n %s" % collections.Counter(str1))
print(collections.Counter(str1)['to'])