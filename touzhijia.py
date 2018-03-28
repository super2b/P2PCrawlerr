# -*- coding: utf-8 -*-
#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  
  try:
    bsObj = BeautifulSoup(html, 'html.parser')
    title = bsObj.head.title
  except AttributeError as e:
    return None
  return title

i = 1
continueLoopThePage = True
while i <= 5:
  targetUrl = str('https://www.touzhijia.com/debt/regulars/all?page=%d&limit=30'  %(i))  
  title = getTitle(targetUrl)
  if title:
    print('the title of page %d: %s' % (i, title))
  i += 1

