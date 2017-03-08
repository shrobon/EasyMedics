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
import cube 

########## Global Variables ###############
file  = ""  # contains the filename selected by the user
directory = None # contains the path to dataset , selected by user 
saveFileName = None  # user-given name to save the VTK produced output with JPEGWRITER

actor = None
render = None 
renWindow = None
renWinInteract = None 

############################################


root = Tk()
root.title("EASY MEDICS (Medical Visualizations made Easy)")
######## MENUBAR SECTION ####################################
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
### File Menu 
######## Open File
def OpenFile():
    # To open a file
    global file 
    file = askopenfilename()
    print file
    #To flush out the print output buffers
    sys.stdout.flush() 
    check()

filemenu.add_command(label="Open File",command = lambda: OpenFile())
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



def check():
    if file != "":
        print "Entered "
        sys.stdout.flush()
        #means that file or directory has been selected and we can display
        #global actor
        #global render
        #global renWindow
        #global renWinInteract
        actor,render,renWindow,renWinInteract = cube.returnCubeObjects(root)              
        renWinInteract.Initialize()
        renWinInteract.pack( fill='both', expand=1)
        renWinInteract.Start()
        renWindow.Render()

        ### Choosing Background Color :: Button
        bgColor = Button(leftFrame,text="Background Colour", bg="orange",command= lambda:BgColor(render,renWindow))
        bgColor.grid(row=0,column=0,sticky=W,pady = 10, padx = 10)

        fgColor = Button(leftFrame,text="Foreground Colour", fg="orange", bg="darkgreen", command= lambda:FgColor(actor,renWindow))
        fgColor.grid(row=0,column=1,sticky=E,pady = 10, padx = 10)
        root.update()
        #######################################################
        ######################################################
    else: 
        print "Bleh"
        sys.stdout.flush()
root.after(1000,check)
root.mainloop()


