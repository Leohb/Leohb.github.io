#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'chap3 query weather with Caiyun API'

__author__ = 'Lei Yunhe'

import requests, json

url = "http://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/116.467,39.9/forecast.json"


r = requests.get(url)
print(r.url)
print(r.text)

# with open("log.txt", 'wb') as fd:
# 	for chunk in r.iter_content(chunk_size):
# 		fd.write(chunk)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)




# TAkhjf8d1nlSlspN

# headers = {'apikey':'TAkhjf8d1nlSlspN'}
# params = {''}

# data = json.dumps({'city':'test','description':'some test repo'})
# r = requests.get(url, data, anth = ('user','TAkhjf8d1nlSlspN'))
