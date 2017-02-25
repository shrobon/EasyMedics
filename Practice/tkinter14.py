#usderstanding filechooser
from tkinter import *
from tkinter import filedialog

window = Tk()
frame = Frame(window)
frame.pack()

label_file = Label(frame)
label_file.pack()

def filechooser():
	type_list = [("Python Scripts","*.py"),("Text Files","*.txt")]
	file_name = filedialog.askopenfilename(filetypes=type_list)
	label_file.config(text=file_name)



button_open = Button(frame,text="Choose a file ...",command=filechooser)
button_open.pack()

window.mainloop()