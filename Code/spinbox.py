from Tkinter import *
import sys

master = Tk()
def show():
    print w.get()
    sys.stdout.flush()

w = Spinbox(master, from_=0, to=10)
w.pack()
x = Button(text="GET",command=show)
x.pack()
mainloop()