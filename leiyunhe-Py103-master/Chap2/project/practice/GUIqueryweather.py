
import tkinter  as tk
from tkinter import *
import 1w-queryV1.1

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "帮助"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")
		self.quit = tk.Button(self, text="退出", fg="red", command=root.destroy)
		self.quit.pack(side="bottom")


	def say_hi(self):
		print("帮助文档：通过输入城市名，查询对应天气")

	def print_contents(self, event):
		print("hi, contents of entry is now >", self.contents.get())

root = tk.Tk()

text = Text(root)
dict = txt_convert_dict("weather_info.txt")
query_city = city.get() 
text.insert(INSERT, query_city)
text.insert(END, dict[query_city])
text.pack()


app = Application()

tk.Label(root, text = "请输入您要查询的城市:").pack()

city = tk.Entry(root)

city.pack()

tk.Button(root, text = '查询').pack()

app.master.title("查询天气小程序")

app.master.maxsize(1000, 700)

app.mainloop()


# ##############entry 
# def evaluate(event):
#     res.configure(text = "Ergebnis: " + str(eval(entry.get())))
# w = Tk()
# Label(w, text="Your Expression:").pack()
# entry = Entry(w)
# entry.bind("<Return>", evaluate)
# entry.pack()
# res = Label(w)
# res.pack()





# import tkinter as tk
# import os

# def save_data():
#     text = name.get().strip()
#     if text: # checks for empty entries
#         f = open('names.txt', 'a')
#         f.write(text + '\n')
#         f.close()
#         name.delete(0, tk.END)

# # Checks if the file exists
# # if not then create it and
# # write the header 'Name List'
# if not os.path.exists('names.txt'):
#     f = open('names.txt', 'w')
#     f.write('Name_List:\n')
#     f.close()

# root = tk.Tk()

# tk.Label(root, text = "Please Enter Name Here:").pack()

# name = tk.Entry(root)
# name.pack()

# tk.Button(root, text = 'Save', command = save_data).pack()

# root.mainloop()