# -*- coding:utf-8 -*-
import urllib.request
import re

url = "http://www.qiushibaike.com/hot/page/1"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'www.qiushibaike.com' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}

req = urllib.request.Request(url, None ,headers = headers)
oper = urllib.request.urlopen(req)
data = oper.read()
str = data.decode("utf8")
oper.close()
#print(str)

pattern = re.compile('<div class="article.*?>(.*?)</div>', re.S)
items = re.findall(pattern, str)
for item in items:
    print(item)