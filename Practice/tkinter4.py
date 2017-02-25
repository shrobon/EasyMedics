from tkinter import *
root = Tk()
label_1 = Label(root,text = "Name")
label_2 = Label(root,text = "Password")

#This is for the text fields
entry_1 = Entry(root)
entry_2 = Entry(root)

#sticky is used for alignment N= North , E= East == Right
label_1.grid(row=0,column=0,sticky=E)
label_2.grid(row=1,column=0,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

#checkbox
c = Checkbutton(root,text="Keep me Logged in") #Has a value of True or False

#To occupy 2 cells and places it in the center
c.grid(columnspan=2)

root.mainloop()

