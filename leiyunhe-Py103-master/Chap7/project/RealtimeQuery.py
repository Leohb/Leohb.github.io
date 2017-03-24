#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests, json
from requestweather import fetchWeather

def query_realtime(city):
	'''query realtime weather'''
	r = fetchWeather(city)
	result = json.loads(r)
	temperature = result["results"][0]['now']['temperature']
	weather = result["results"][0]['now']['text']
	get_weather = [city,  weather , temperature + "C"]
	#print(type(get_weather[0]), type(get_weather[1]), type(get_weather[2]))
	#log_append(str(get_weather[0]) + str(get_weather[1]) + str(get_weather[2]))
#	log_append(''.join(get_weather))
	return get_weather

def documentation(filename):
	'''打印filename文档的内容'''
	with open(filename, "r") as f:
		return f.read()

def log():
	'''创建日志文件'''
	with open("log.txt", "w") as f:
		f.write(u"您的查询记录如下：\n")

def log_append(content):
	'''增加日志记录'''
	with open("log.txt", "a") as f:
		f.write(content)

if __name__ == "__main__":
	while True:
		user_input = input("请输入城市或指令：")

		if user_input in {"quit", "exit"}:
			break
		elif user_input == "history":
			print(documentation("log.txt"))
		elif user_input == "help":
			print(documentation("README.md"))
		else:
			print(query_realtime(user_input))



