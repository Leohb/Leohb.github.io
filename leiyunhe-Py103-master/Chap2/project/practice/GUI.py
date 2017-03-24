#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quit():
	'''quit'''
	print("本次查询结束！欢迎再次使用！")

def txt_convert_dict(filename):
	'''convert a file(.txt) to a dictionary and return the dictionary'''
	with open(filename,"r", encoding = "utf-8") as f:
		dict = {} #create a dict
		for line in f:
			s = line.split(',')  #split: turning a string with a certain separator into a list.
			dict.setdefault(s[0], s[1])
	return dict

def help():
	'''Help documentaion'''
	with open("README.md","r", encoding = "utf-8") as f:
		print(f.read())

def exception():
	'''user input is not valid'''
	print("您输入的信息有误，请重新输入！")

def query_weather(dict, history):
	'''query weather'''
	print("请输入您要查询的城市或指令： ")
	while True:
		user_input = input()
		if user_input.upper() in {"QUIT", "EXIT", "Q", "E"}:
			quit()
			break
		elif user_input in {"history"}:
			print("您的查询历史如下：")
			for h in history:
				print(h + "的天气情况是" + dict[h])			
		elif user_input in {"help"}:
			help()
		elif user_input in dict:
			# if user_input not in history:  # remove duplicate elements
			# 	history.append(user_input)
			print(user_input + "天气：" + dict[user_input])
		else:
			exception()

if __name__ == '__main__':
	city_weather = txt_convert_dict("weather_info.txt")
	query_history = []
	query_weather(city_weather, query_history)



