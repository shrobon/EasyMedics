from tkinter import *
from PIL import Image, ImageTk
from tkinter import PhotoImage
root = Tk()
im = Image.open("twitter-128.png")
ph = ImageTk.PhotoImage(im)
#currently pictures are working only with gif

photo = PhotoImage(file = ph)
label = Label(root,image=photo)
label.pack()
root.mainloop()