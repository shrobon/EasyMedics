from tkinter import *
root = Tk()

def leftClick(event):
	print("left")

def middleClick(event):
	print("middle")

def rightClick(event):
	print("right")

frame = Frame(root,width=300,height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)

frame.pack()



root.mainloop()