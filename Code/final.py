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
from guifunctions import * #Contains all the event functions code

########## Global Variables ###############
file  = None  # contains the filename selected by the user
directory = None # contains the path to dataset , selected by user 
saveFileName = None  # user-given name to save the VTK produced output with JPEGWRITER
############################################



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




root = Tk()
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
filemenu.add_command(label= "Exit" , command = root.quit)
##############################################################

renWinInteract = vtkTkRenderWindowInteractor(root,rw=renWindow, width=600, height=600)                   
renWinInteract.Initialize()
renWinInteract.pack(side='top', fill='both', expand=1)
renWindow.Render()
######################################################

renWinInteract.Start()
root.mainloop()


