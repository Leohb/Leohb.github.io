from tkinter import *

root = Tk()
logo = PhotoImage(file="pic/bird.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, there are a image"""
w2 = Label(root, justify=LEFT, padx = 10, text= explanation).pack(side="left")
root.mainloop()