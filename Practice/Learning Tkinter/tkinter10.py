from tkinter import *

def doNothing():
	print("I wont !! ")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
#dropdown is known as cascading in tkinter
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_command(label="Open",command=doNothing)
subMenu.add_separator() # draws a line
subMenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

#Toolbar
toolbar = Frame(root,bg="blue")
insertButt = Button(toolbar,text="Inset Image",command=doNothing)
insertButt.pack(side=LEFT,padx=2,pady=2)

printButt = Button(toolbar,text="Print",command=doNothing)
printButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)
root.mainloop()