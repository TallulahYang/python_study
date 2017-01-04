#! /usr/bin/env python3
# coding: utf-8

# 分析html

from bs4 import BeautifulSoup
import requests

url='https://cn.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html';
wt_data = requests.get(url)
soup = BeautifulSoup(wt_data.text,'lxml')
titles = soup.select('div.listing_title > a')
for i in titles:
    data ={
        'title': i.get_text()
    }
    print(data)