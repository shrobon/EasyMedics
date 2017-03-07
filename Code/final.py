import sys
if sys.hexversion < 0x03000000:
    # for Python2
    from Tkinter import *
else:
    # for Python3
    from tkinter import *
import vtk
from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor
from tkFileDialog import *


def OpenFile():
    # To open a file
    file = askopenfilename()
    print file
    #This line is necessary to flush out the print output buffers
    sys.stdout.flush() 

def OpenFolder():
    # To open a direcotry
    directory = askdirectory(initialdir='.')
    print directory
    sys.stdout.flush()


root = Tk()

######## MENUBAR SECTION ####################################
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
### File Menu 
######## Open File
filemenu.add_command(label="Open File",command = OpenFile)
filemenu.add_command(label="Open Folder",command= OpenFolder)
filemenu.add_separator()
### Exit Option
filemenu.add_command(label= "Exit" , command = root.quit)
##############################################################
root.mainloop()


