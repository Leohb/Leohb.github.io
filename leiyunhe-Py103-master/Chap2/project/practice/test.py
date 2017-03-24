from tkinter import *
import QueryWeather as qw

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

def callback():
	text.config(state=NORMAL)
	if e.get():
		print(e.get())
		str = qw.query(e.get(), qw.txt_convert_dict("weather_info.txt"))
		text.insert(END, str)
		print(str)
		e.delete(0, END)
	text.config(state=DISABLED)

def print_help():
	text.config(state=NORMAL)
	str = qw.help()
	text.insert(END, str)
	print(qw.help())
	text.config(state=DISABLED)

def print_log():
	text.config(state=NORMAL)
	with open("log.txt", "r", encoding = "utf-8") as f:
		text.insert(END, f.read())
		print(f.read())
	text.config(state=DISABLED)	



Button(master, text="查询", width=10, command = callback).pack(side = "left")
Button(master, text="历史", width=10, command = print_log).pack(side = "left")
Button(master, text="帮助", width=10, command = print_help).pack(side = "left")
Button(master, text="退出", width=10, command = master.destroy).pack(side = "left")



mainloop()