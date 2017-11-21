#!/usr/bin/env python
from fetch import fetch
from sys import exit

URL = ('https://raw.githubusercontent.com/exercism/'
       'problem-specifications/master/TOPICS.txt')
exit(fetch(URL))
