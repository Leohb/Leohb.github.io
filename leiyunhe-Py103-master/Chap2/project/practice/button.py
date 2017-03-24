from tkinter import *
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.button = Button(frame, text = "QUIT", fg = "red", command=quit)
		self.button.pack(side="left")
		self.slogan = Button(frame, text = "hello", command= self.write_slogan)
		self.slogan.pack(side="left")
	def write_slogan(self):
		print("TKinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()
