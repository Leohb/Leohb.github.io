#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

url = 'http://wiki.swarma.net/index.php/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94%E4%B8%BB%E8%A6%81%E5%9F%8E%E5%B8%82%E6%9F%A5%E8%AF%A2%E5%9C%B0%E5%9D%80%E5%88%97%E8%A1%A8'
r = requests.get(url)

soup = BeautifulSoup(r.text)

data = soup.select("table tr td")

dict = {}

for num in range(1,193,4):
	dict(data[num].string) = data[num + 1].string

for line in dict:
	print(line)
	print(json.dumps(line, separators = ('<td>', '</td>'),)


query_url = 


