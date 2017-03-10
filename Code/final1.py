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
import heart

########## Global Variables ###############
file  = ""  # contains the filename selected by the user
directory = None # contains the path to dataset , selected by user 
saveFileName = None  # user-given name to save the VTK produced output with JPEGWRITER
partNumber = -999 # Contains the tissue number for MRI / CT Dataset
color_array = []
parts_array = []

actor = None
render = None 
renWindow = None
renWinInteract = None 
############################################

root = Tk()
v = IntVar() # keeps the state of the radiobuttons
root.title("EASY MEDICS (Medical Visualizations made Easy)")




######## MENUBAR SECTION ####################################
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
### File Menu 

######## Open File
def OpenFile():
    # This function is triggered when the user chooses to Open a file 
    global file 
    file = askopenfilename()
    print file
    #To flush out the print output buffers
    sys.stdout.flush() 
    selected_radio_value = v.get()
    if selected_radio_value == 0:
        # Nothing has beeen selected yet
        # Alert the user to select some radio-button
        showerror("Error", "Error: Select a radio button first, and then try again ..")
    elif selected_radio_value == 1: #Radio CUBE-Source
        CubeDisplay() # Open the vtk-cube source program 
    elif selected_radio_value == 2:
        HeartDisplay()
    else:
        pass
        

filemenu.add_command(label="Open File",command = lambda: OpenFile())
######## Open Folder
filemenu.add_command(label="Open Folder",command= OpenFolder)
filemenu.add_separator()
######## Save Options
#filemenu.add_command(label="Save",command= lambda: SaveOutput(renWindow))
#filemenu.add_separator()

### Exit Option
#filemenu.add_command(label= "Exit" , command = lambda: Quit(root))
##############################################################


############# Interaction Controls ########################
leftFrame = Frame(root)
leftFrame.pack(side=LEFT,expand=1)

### Radio Buttons for selecting the type of project 

projects = [
    ("Cube Source",1),
    ("Volume Rendering",2),
    ("STL / BYU",3)
]

def CheckRadioChoice():
    print v.get() #displays the users radio button choice
    sys.stdout.flush()


row = 0
for text,val in projects:
    x = Radiobutton(leftFrame,
    text=text,
    padx = 20,
    variable = v,
    command=CheckRadioChoice,
    value= val)
    x.grid(row=row,column=0,sticky=W)
    row = row + 1
##################################################


def CubeDisplay():
    if file != "":
        #print "Entered "
        #sys.stdout.flush()
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
        bgColor.grid(row=row,column=0,sticky=W,pady = 10, padx = 10)

        fgColor = Button(leftFrame,text="Foreground Colour", fg="orange", bg="darkgreen", command= lambda:FgColor(actor,renWindow))
        fgColor.grid(row=row,column=1,sticky=E,pady = 10, padx = 10)

        #Save Output Option
        filemenu.add_command(label="Save",command= lambda: SaveOutput(renWindow))
        filemenu.add_separator()
        #root.update()
        #######################################################
        ######################################################



def TissueColor(partNumber,colorFunc,renWindow):
    # This is a colout picker for tissue
    partNumber = int(partNumber)
    print partNumber
    sys.stdout.flush()

    if partNumber != -999:
        color = askcolor(color="#6B7722",title="Foreground Color")
        color = color[0]
        (r,g,b) = color # RGB tuple 
        r = float("{0:.2f}".format(r/255))
        g = float("{0:.2f}".format(g/255))
        b = float("{0:.2f}".format(b/255))
        colorFunc.AddRGBPoint(partNumber,r, g, b)
        rgbValue = [r,g,b]
        color_array.append(rgbValue)
        parts_array.append(partNumber)

    else:
        #Show an error dialog :: Select part number first
        showerror("Error", "Error: Select a tissue number first, and then try again ..")

def HeartDisplay():
    if file !="":
        volumeMapper,volume,render,renWindow,renWinInteract,colorFunc,alphaChannelFunc,volumeProperty = heart.returnHeartObjects(root)
        v= StringVar()
        v.set("-999")
        ### Choosing a Tissue Number 
        Tissue = Entry(leftFrame,text="int",textvariable=v)
        Tissue.grid(row=row,column=0,sticky=W,pady=10,padx=10)
        
        ### Choosing the Tissue Colour
        partNumber = int(v.get())
        tissueColor = Button(leftFrame,text="Tissue Colour", bg="orange",command= lambda:TissueColor(int(v.get()),colorFunc,renWindow))
        tissueColor.grid(row=row,column=1,sticky=W,pady = 10, padx = 10)
        '''
        colorFunc.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
        colorFunc.AddRGBPoint(-77, 0.54902, 0.25098, 0.14902)
        colorFunc.AddRGBPoint(94, 0.882353, 0.603922, 0.290196)
        colorFunc.AddRGBPoint(179, 1, 0.937033, 0.954531)
        colorFunc.AddRGBPoint(260, 0.615686, 0, 0)
        colorFunc.AddRGBPoint(3071, 0.827451, 0.658824, 1)
        '''

        alphaChannelFunc.AddPoint(-3024, 0.0)
        alphaChannelFunc.AddPoint(-77, 0.0)
        alphaChannelFunc.AddPoint(94, 0.29)
        alphaChannelFunc.AddPoint(179, 0.55)
        alphaChannelFunc.AddPoint(260, 0.84)
        alphaChannelFunc.AddPoint(3071, 0.875)

        volumeProperty.SetScalarOpacity(alphaChannelFunc)
        volumeProperty.SetColor(colorFunc)
        volumeProperty.ShadeOn()

        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)
        render.AddVolume(volume)

        renWinInteract.Initialize()
        renWinInteract.pack( fill='both', expand=1)
        renWinInteract.Start()
        renWindow.Render()


        
        #Save Output Option
        filemenu.add_command(label="Save",command= lambda: SaveOutput(renWindow))
        filemenu.add_separator()
        #root.update()
        #######################################################
        ######################################################


### Exit Option
filemenu.add_command(label= "Exit" , command = lambda: Quit(root))
##############################################################
#root.after(1000,check)
root.mainloop()


