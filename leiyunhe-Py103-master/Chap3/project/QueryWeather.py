#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import strftime, localtime

def quit():
	'''quit'''
	return "本次查询结束！欢迎再次使用！"

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
		return f.read()

def query(item, dict):

	if item in dict:
		str = item + "的天气：" + dict[item]
	else:
		str = "不存在，请重新输入规范信息\n"
	str = strftime("%Y-%m-%d, %H:%M:%S", localtime()) + str
	log(str)
	return str

def log(str):
	with open("log.txt", "a", encoding = "utf-8") as f:
		f.write(str)
	return f

if __name__ == '__main__':
	city_weather = txt_convert_dict("weather_info.txt")

	with open("log.txt", "w", encoding = "utf-8") as f:
		f.write("您的查询记录如下：\n")

	while True:
		user_input = input("请输入城市或指令:")
		if user_input in {"exit", "quit"}:
			print(quit())
			break
		elif user_input == "history":
			with open("log.txt", "r", encoding = "utf-8") as f:
				print(f.read())
		elif user_input == "help":
			print(help())
		else:
			print(query(user_input, city_weather))
	

	mainloop()






