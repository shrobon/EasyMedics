from __future__ import division
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
from tkMessageBox import *
from tkColorChooser import askcolor
from guifunctions import * #Contains all the event functions code


########## Global Variables ###############
file  = None  # contains the filename selected by the user
directory = None # contains the path to dataset , selected by user 
saveFileName = None  # user-given name to save the VTK produced output with JPEGWRITER
############################################


root = Tk()
cube = vtk.vtkCubeSource()
cube.Modified()
mapper = vtk.vtkPolyDataMapper()
actor = vtk.vtkActor()

mapper.SetInputConnection(cube.GetOutputPort())
actor.SetMapper(mapper)
render = vtk.vtkRenderer()
render.AddActor(actor)

renWindow = vtk.vtkRenderWindow()
renWindow.AddRenderer(render)


root.title("EASY MEDICS (Medical Visualizations made Easy)")
######## MENUBAR SECTION ####################################
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
### File Menu 
######## Open File
filemenu.add_command(label="Open File",command = OpenFile)
######## Open Folder
filemenu.add_command(label="Open Folder",command= OpenFolder)
filemenu.add_separator()
######## Save Options
filemenu.add_command(label="Save",command= lambda: SaveOutput(renWindow))
filemenu.add_separator()

### Exit Option
filemenu.add_command(label= "Exit" , command = lambda: Quit(root))
##############################################################


############# Interaction Controls ########################
leftFrame = Frame(root)
leftFrame.pack(side=LEFT,expand=1)

### Choosing Background Color :: Button
bgColor = Button(leftFrame,text="Background Colour", bg="orange",command= lambda:BgColor(render,renWindow))
bgColor.grid(row=0,column=0,sticky=W,pady = 10, padx = 10)

fgColor = Button(leftFrame,text="Foreground Colour", fg="orange", bg="darkgreen", command= lambda:FgColor(actor,renWindow))
fgColor.grid(row=0,column=1,sticky=E,pady = 10, padx = 10)
#######################################################


renWinInteract = vtkTkRenderWindowInteractor(root,rw=renWindow, width=800, height=800)                   
renWinInteract.Initialize()
renWinInteract.pack( fill='both', expand=1)
renWindow.Render()
######################################################

renWinInteract.Start()
root.mainloop()


