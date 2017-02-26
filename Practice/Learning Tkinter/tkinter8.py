from tkinter import *

class Shrobon:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame,text="Print Message",command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quit = Button(frame,text="Quit",command=frame.quit)
		self.quit.pack(side=LEFT)

	def printMessage(self):
		print(" Wow this works !! ")

root = Tk()
b = Shrobon(root)
root.mainloop()
