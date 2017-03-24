
# 代码分析

本周的任务难点主要有两个：第一是对w1代码的改写。需要提炼核心功能。第二是GUI中控件的响应事件。从命令行互动，发展到图形界面交互。

## w1代码改写为可复用的函数
对w1中CLI程序的改写，使其可复用。这需要将程序的功能剥离开来，分别定义函数，每个函数只能实现一个独立的功能。这样就能够将其导入到w2中重复使用。这样做的好处时，在后续编写代码的时候，不至于又重新从头写代码，而是可以直接使用已经写好的功能模块。

对于没有编程基础（尤其是没有面向对象编程知识）的人来说，提炼出核心功能是非常困难的。通过w1到w2的练习，可以发现：写出独立核心功能函数的关键有三点：

+ 传入的形式参数
+ 实现本函数功能的程序
+ 函数的返回值

这些都是C语言编程中学习过的基础知识。但是，当真正动手编程的时候，主要将思路厘清，就会函数功能是比较好实现的，但是，需要写出优美而精练的代码，就需要关注“传入形式参数”和“函数的返回值”这两项，这两项看似简单，但其实相对比较难。可能需要注意的知识点如下：

+ 实际参数（形式参数）的数据类型（str、list、dict、tuple等）
+ 在主函数中定义全局变量
+ 函数返回值传递回主函数，并应用于主函数（不要直接在函数定义中print等操作）。这样可以让功能更独立。
+ 函数返回值作为参数，可以放到哪些位置（比如print，某个函数中的参数等。）

## 通过GUI控件实现图形化的人机交互

GUI（Graphical User Interface）这个词往往会吓到我们。这个词给我们一种很高大上的感觉（比起w1中的CLI程序）。这让人误以为这样的程序不同于我们在CLI中的程序。因此，在最初的摸索中，我一直以为GUI程序使用的是完全不同于CLI端程序的架构和结构。实际上，GUI运行程序只是将CLI端程序进行包装，也就是完成界面交互设计。w2作业结果表明：GUI的代码框架结构与CLI的大体相同，只不过应用的模块不一样。

GUI界面的构建使用Tkinter模块，可以构建出文本框、按钮等基本的控件。这些都是比较简单的，找到官方文档中的案例，或者自己搜索一些tutorial，跟着做几个例子，就自然明白了。但问题是，官方文档（tkinter这一块的例子比较少）、各种tutorial中找到的例子和我们要完成的任务还是有差别的。那么，修改这些例子的过程，就是学习和熟悉这个模块及文档的过程。我没有找到与w2任务完全相同的例子，那么，这些差异就需要发挥自学能力，进行摸索和尝试的地方。这给我的经验是，以后在写其他程序的时候，最好是首先提炼核心功能，然后寻找与核心功能类似的例子。通过对例子的研读和修改，完成自己的程序功能。

控件的响应事件，这个是最难的部分。具体说，有：

+ 输入entry的值
+ 点击“查询”按钮
  - 将entry的值传入处理过程
  - 将处理结束的值显示到text
+ text的状态设置：text的disable、normal的状态处理，保证text文本框不能直接获取从键盘的输入值。

实际上，在具体的程序中，【查询】【帮助】【日志】需要完成的工作是相同的，以【查询】为例，可分解如下：

+ 定义一个全局变量e，保存entry的值
+ “查询”按钮的command参数，抽离出来，写成一个独立函数模块(callback)
+ callback中，将全部变量e的值，调用ch1(QueryWeather.py)字典查询程序，得到天气信息后，将其通过text.insert插入到text的显示文本中。
+ text的状态通常设置为disable，在需要insert的时候，就改为normal，结束后再变成disable。

## 优化设计

程序名称：
按钮排布：
字体颜色：
bind：输入文字后直接回车查询



# 附：源文件WeatherQueryGUI.py

```
from tkinter import *
import QueryWeather as qw

def callback():
	#点击查询按钮，将查询结果输出到文本显示区域
	text.config(state=NORMAL)
	if e.get():
		print(e.get())
		str = qw.query(e.get(), qw.txt_convert_dict("weather_info.txt"))
		text.insert(END, str)
		print(str)
		e.delete(0, END)
	text.config(state=DISABLED)

def print_help():
	#点击帮助按钮，将帮助文档显示到文本显示区域
	text.config(state=NORMAL)
	str = qw.help()
	text.insert(END, str)
	print(qw.help())
	text.config(state=DISABLED)

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

# 附：导入模块文件WeatherQuery.py

```
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
		user_input = input("请输入城市:")
		if user_input == "history":
			with open("log.txt", "r", encoding = "utf-8") as f:
				print(f.read())
		print(query(user_input, city_weather))
mainloop()
```


