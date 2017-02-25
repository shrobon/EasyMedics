#binding a function to a widget
from tkinter import *
root = Tk()

def printName():
	print("My name is Shrobon")

button_1 = Button(root,text="Print my name",command= printName)
button_1.pack()
root.mainloop()