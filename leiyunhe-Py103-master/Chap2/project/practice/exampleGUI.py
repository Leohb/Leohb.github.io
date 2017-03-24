
import tkinter  as tk
from tkinter import *
import QueryWeather

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.help = tk.Button(self)
		self.help["text"] = "帮助"
		self.help["width"] = 8
		self.help["command"] = QueryWeather.help()
		self.help.pack(side="right")

		self.history = tk.Button(self)
		self.history["text"] = "历史"
		self.history["width"] = 8		
		self.history["command"] = self.log
		self.history.pack(side="right")

		self.quit = tk.Button(self, text="退出", width= 8, fg="red", command=root.destroy)
		self.quit.pack(side="right")

		self.note = tk.Label(self)
		self.note["text"] = "请输入您要查询的城市："
		self.note.pack(side = "left")

		self.entry = tk.Entry(self)
		self.entry["width"] = 15
		#self.entry.bind("<Return>", query)
		self.entry.pack(side="left")

		self.query = tk.Button(self)
		self.query["text"] = "查询"
		self.query["width"] = 8
		self.query["command"] = self.query_weather
		self.query.pack(side="right")

	def query_weather(self):

		print("从字典中查询天气")


	def log(self):
		print("历史记录与查询日志")

	def print_contents(self, event):
		print("hi, contents of entry is now >", self.contents.get())


root = tk.Tk()


# text = Text(root)
# text.insert(INSERT, city)

# text.insert(END, city*2)
# text.pack()
app = Application(root)
root.mainloop()



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