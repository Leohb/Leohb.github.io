# 分析chap3编写的几个版本：

## V1.1 CLI版本

```
import requests, json

def query_realtime():
	'''query realtime weather'''
	r = requests.get(url)
	result = json.loads(r.text)
	city = result["results"][0]['location']['name']
	realtime = result["results"][0]['last_update']
	temperature = result["results"][0]['now']['temperature']
	weather = result["results"][0]['now']['text']

	return city + realtime + "天气情况为：" + weather + "," + "温度："+ temperature + "摄氏度"


with open("log.txt", "w", encoding = "utf-8") as f:
	f.write("您的查询记录如下：\n")


while True:

	user_input = input("请输入城市或指令：")

	if user_input in {"quit", "exit"}:
		break
	elif user_input == "history":
		with open("log.txt", "r", encoding = "utf-8") as f:
			print(f.read())
	elif user_input == "help":
		with open("README.md", "r", encoding = "utf-8") as f:
			print(f.read())
	else:
		url = "https://api.thinkpage.cn/v3/weather/now.json?key=kdtkmkoewxfhmqbx&location=" + user_input + "&language=zh-Hans&unit=c"
		get_weather = query_realtime()
		
		with open("log.txt", "a", encoding = "utf-8") as f:
			f.write(get_weather + "\n")
		print(get_weather)


```


## V2.1 GUI版本

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import requests, json

def query_realtime(url):
	'''query realtime weather'''
	r = requests.get(url)
	result = json.loads(r.text)
	city = result["results"][0]['location']['name']
	realtime = result["results"][0]['last_update']
	temperature = result["results"][0]['now']['temperature']
	weather = result["results"][0]['now']['text']

	str = city + realtime + "天气情况为：" + weather + "," + "温度："+ temperature + "摄氏度"
	log(str)
	return str


def callback():
	#点击查询按钮，将查询结果输出到文本显示区域
	text.config(state=NORMAL)
	if e.get():
		print(e.get())
		str1 = e.get()
		url = "https://api.thinkpage.cn/v3/weather/now.json?key=kdtkmkoewxfhmqbx&location=" + str1 + "&language=zh-Hans&unit=c"
		str2 = query_realtime(url) + "\n"
		text.insert(END, str2)
		print(str2)
		e.delete(0, END)
	text.config(state=DISABLED)

def print_help():
	#点击帮助按钮，将帮助文档显示到文本显示区域
	text.config(state=NORMAL)

	with open("README.md", "r", encoding = "utf-8") as f:
		str = f.read()

	text.insert(END, str)
	print(str)
	text.config(state=DISABLED)

def log(str):
	with open("log.txt", "a", encoding = "utf-8") as f:
		f.write(str + "\n")
	return f

def print_log():
	#打印查询日志
	text.config(state=NORMAL)
	with open("log.txt", "r", encoding = "utf-8") as f:
		text.insert(END, f.read())
		print(f.read())
	text.config(state=DISABLED)	

if __name__ =='__main__':
	master = Tk()
	master.title("天气查询小程序")

	text = Text(master)
	text.pack()
	text.config(state=DISABLED)

	with open("log.txt", "w", encoding = "utf-8") as f:
		f.write("您的查询历史如下：\n")

	Label(master, text = "请输入城市名称：").pack(side = "left")

	e = Entry(master)
	e.pack(side = "left")
	e.focus_set()



	Button(master, text="查询", width=10, command = callback).pack(side = "left")

	Button(master, text="历史", width=10, command = print_log).pack(side = "left")
	Button(master, text="帮助", width=10, command = print_help).pack(side = "left")
	Button(master, text="退出", width=10, command = master.destroy).pack(side = "left")

	mainloop()



```

## V3.1 

```
进阶任务

```