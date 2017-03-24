from tkinter import *
import QueryWeather as qw

def callback(e):
	```点击查询按钮，将查询结果输出到文本显示区域```
	text.config(state=NORMAL)
	if e.get():
		print(e.get())
		str = qw.query(e.get(), qw.txt_convert_dict("weather_info.txt"))
		text.insert(END, str)
		print(str)
		e.delete(0, END)
	text.config(state=DISABLED)

def print_help():
	```点击帮助按钮，将帮助文档显示到文本显示区域```
	text.config(state=NORMAL)
	str = qw.help()
	text.insert(END, str)
	print(qw.help())
	text.config(state=DISABLED)

def print_log():
	```打印查询日志```
	text.config(state=NORMAL)
	with open("log.txt", "r", encoding = "utf-8") as f:
		text.insert(END, f.read())
		print(f.read())
	text.config(state=DISABLED)	

if __name__ =='__main__':
	master = Tk()
	master.title("天气查询小程序")




	with open("log.txt", "w", encoding = "utf-8") as f:
		f.write("您的查询历史如下：\n")

	Label(master, text = "请输入城市名称：").pack(side = "left")

	input = Entry(master)
	input.pack(side = "left")
	input.focus_set()


	text = Text(master)
	text.pack()
	#text.config(state=DISABLED)

	text.bind('<Return>', (lambda event, e = input: callback(e)))
	b =  Button(master, text="查询", width=10, command = (lambda event, e = input: callback(e)))
	b.pack(side = "left")
	#Button(master, text="查询", width=10, command = callback(input)).pack(side = "left")

	Button(master, text="历史", width=10, command = print_log).pack(side = "left")
	Button(master, text="帮助", width=10, command = print_help).pack(side = "left")
	Button(master, text="退出", width=10, command = master.destroy).pack(side = "left")

mainloop()

	root = Tk()
	ents = makeform(root, fields)
	root.bind('<Return>', (lambda event, e= ents: fetch(e)))
	b1 = Button(root, text='show', command=(lambda e=ents: fetch(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(root, text='Quit', command=root.quit)
	b2.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()