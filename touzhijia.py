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

def getDesc(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  
  try:
    bsObj = BeautifulSoup(html, 'html.parser')
    desc = bsObj.find('meta',{'name':'description'})
  except AttributeError as e:
    return None
  return desc.attrs['content']

def getContent(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  
  contents = []
  try:
    bsObj = BeautifulSoup(html, 'html.parser')
    trs = bsObj.tbody.findAll('tr')
    for t in trs:
      contents.append(t.td.a.text)
      detailUrl = t.td.a.attrs['href']
      print(detailUrl)
      try:
        if not str(detailUrl).startswith('http'):
          detailUrl = "http:" + str(detailUrl)
        detailHtml = urlopen(detailUrl)
        detailBsObj = BeautifulSoup(detailHtml, 'html.parser')
        desc = detailBsObj.find('div', {'id':'description'}).findAll('td')[0].p.text
        print(desc)
      except HTTPError as e:
        return None
  except AttributeError as e:
    return None
  return contents

page = 1
pageSize = 20
targetUrl = str('https://www.touzhijia.com/debt/regulars/all?page=%d&limit=%d'  %(page,pageSize))  
desc = getDesc(targetUrl)
print(desc)
###########

continueLoopThePage = True
finalContents = []
while page <= 3:
  content = getContent(targetUrl)
  if content:
    finalContents.extend(content)
  page += 1

i = 1
for c in finalContents:
  print('%i:%s\n' %(i, c))
  i += 1

