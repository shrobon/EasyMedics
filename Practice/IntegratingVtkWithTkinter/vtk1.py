from Tkinter import * 
import vtk
import sys
from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor


#Initializing the parent window of tkinter
root = Tk()
root.title(" My first Tk & vTk GUI")

#creating a frame
frame = Frame(root)
frame.pack(fill = "both",side="top")

root.mainloop()

