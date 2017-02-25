from tkinter import *
from tkinter import messagebox
import os
root = Tk()

messagebox.showinfo('Alert Title','Hello World')
answer = messagebox.askquestion('Question 1','Do you like silly faces !')
if answer == 'yes':
	print('Awesome !! ')
else:
	print('Boo')

root.mainloop()