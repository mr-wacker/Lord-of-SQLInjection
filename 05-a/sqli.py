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



admin = '0x61646d696e'

''' white space other than \x20
newline : \n \x0a
horizontal tab : \t \x13
vertical tab : \v \x09
backspace : \b
carriage return : \r \x0d
formfeed : \f
audible alert : \a
'''

# https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?pw=%27%0Aor%0Aid=%27admin%27%0A%23
