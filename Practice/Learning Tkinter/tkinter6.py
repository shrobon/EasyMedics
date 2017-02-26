from tkinter import *
root = Tk()

def printName(event):
	print "Hello World"

button_1 = Button(root,text= "Print Hello World")
#the button tag here refers to the left mouse button
button_1.bind("<Button-1>",printName)

root.mainloop()