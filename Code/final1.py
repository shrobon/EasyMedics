# __Author__ : Shrobon Biswas
# __Start_Date__ : 1/3/2017
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
opacity_array = [] # stores the user selected opacity value for a specific tissue
action_log_messages = [] # Stores the messages in the Action Logs
# Whenever a new action is performed, the action is added to the beginning of the list
listbox = None
row = 0 # Keeps track of the UI-element rows
off = 0

actor = None
render = None
renWindow = None
renWinInteract = None

volumeMapper = None
volume = None
colorFunc= None
alphaChannelFunc = None
volumeProperty = None
x = None # This is the radiobutton :: I will destroy this when i enter a project
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
    ("Volume Rendering",2)
]

def CheckRadioChoice():
    print v.get() #displays the users radio button choice
    sys.stdout.flush()


row = 0



def check():
    ## This part is not helping for the UI overlap :: root.update is adding extra performance issues
    global off
    if off == 0:
        off = 1
        global row,x
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
check()

def CubeDisplay():
    if file != "":
        global off
        off = 1
        global x
        x.destroy()
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



def TissueColor(partNumber,opacity,colorFunc,alphaChannelFunc,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow):
    # This is a colout picker for tissue

    global parts_array
    global opacity_array
    global color_array
    global action_log_messages
    global listbox

    partNumber = int(partNumber)
    #print partNumber
    #sys.stdout.flush()

    opacity = float("{0:.2f}".format(opacity/100))
    #print opacity
    #sys.stdout.flush()

    if partNumber != -999:
        color = askcolor(color="#6B7722",title="Foreground Color")
        color = color[0]
        (r,g,b) = color # RGB tuple
        r = float("{0:.2f}".format(r/255))
        g = float("{0:.2f}".format(g/255))
        b = float("{0:.2f}".format(b/255))
        #colorFunc.AddRGBPoint(partNumber,r, g, b)
        if partNumber in parts_array:
            # if part is already in parts array then no need to add to array:: Modify the array elements
            index = parts_array.index(partNumber)
            # change tissue color , opacity , at the obtained index
            color_array[index] = [r,g,b] #These are the new rgb VALUES
            opacity_array[index] = opacity


        else:
            rgbValue = [r,g,b]
            color_array.append(rgbValue)
            parts_array.append(partNumber)
            opacity_array.append(opacity)

            ##### Inserting a log entry to action_log_messages   ##########
            temp = "Added Part #:%d, R:%f,G:%f,B:%f,Opacity:%f\n"%(partNumber,r,g,b,opacity)
            action_log_messages.insert(0,temp)

            listbox = Text(leftFrame,height=10,width=45)
            listbox.grid(row = row+3,columnspan=3,sticky=W,pady=10,padx=10)
            scrollbar = Scrollbar(leftFrame)
            scrollbar.grid(row = row+3,column=3,sticky=W,pady=10,padx=10)

            for i in range(len(action_log_messages)):

                listbox.insert(END,action_log_messages[i])

            listbox.config(yscrollcommand = scrollbar.set)
            scrollbar.config(command = listbox.yview)
            ###############################################################

        #So now send the acquired arrays for rendering
        RenderTissues(colorFunc,alphaChannelFunc  ,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow)

    else:
        #Show an error dialog :: Select part number first
        showerror("Error", "Error: Select a tissue number first, and then try again ..")


def RenderTissues(colorFunc,alphaChannelFunc,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow):
    #loop over the total number of Tissues in Tissues array and add Color and Opacity
    global parts_array
    global opacity_array
    global color_array

    #### Description : For Realtime addition and deletion of ColorFunction Points#####################
    colorFunc.RemoveAllPoints()
    alphaChannelFunc.RemoveAllPoints()
    ##################################################################################################

    print "Length of parts array is = %d"%len(parts_array)
    sys.stdout.flush()
    for i in range(0,len(parts_array)):
        part = parts_array[i]
        color = color_array[i] # this is in form [r,g,b]
        r = color[0]
        g = color[1]
        b = color[2]

        o = opacity_array[i] # this contains the opacity values
        # adding the color values
        colorFunc.AddRGBPoint(part,r,g,b)
        #adding the opacity values
        alphaChannelFunc.AddPoint(part,o)

    if len(parts_array) == 0 :
        # 1 element added first :: then that element has been set for delete
        # we still need to redisplay as the previous loop will not run

        ## PROBLEM HERE : FIRST SET THE VALUES AND THEN DISPLAY


        part = parts_array[0]
        color = color_array[0] # this is in form [r,g,b]
        r = color[0]
        g = color[1]
        b = color[2]
        o = opacity_array[0] # this contains the opacity values
        # adding the color values
        colorFunc.AddRGBPoint(part,r,g,b)
        #adding the opacity values
        alphaChannelFunc.AddPoint(part,o)

    volumeProperty.SetScalarOpacity(alphaChannelFunc)
    volumeProperty.SetColor(colorFunc)
    volumeProperty.ShadeOn()

    volume.SetMapper(volumeMapper)
    volume.SetProperty(volumeProperty)
    render.AddVolume(volume)
    render.ResetCamera()

    renWindow.Render()
    #volume.Modified()






def DeleteColorFunction(part,colorFunc,alphaChannelFunc ,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow):
    global parts_array
    global opacity_array
    global color_array
    global action_log_messages
    #print "Entered Remove Color "
    sys.stdout.flush()

    if part != -999:
        # if it is 999 means that no value has been set
        # Test Case 1 : if the part has been added firstly or not
        #print "part selected is =%d"%part
        if part in parts_array:
            #print "Entered Parts Array"
            #sys.stdout.flush()
            #Yes : The part has been previously added
            #We need to remove the part and the colour values associated with it
            index = parts_array.index(part)

            parts_array.pop(index)
            color_array.pop(index)
            opacity_array.pop(index)

            ##### Inserting a log entry to action_log_messages   ##########
            temp = "Deleted Part #:%d\n"%(part)
            action_log_messages.insert(0,temp)

            listbox = Text(leftFrame,height=10,width=45)
            listbox.grid(row = row+3,columnspan=3,sticky=W,pady=10,padx=10)
            scrollbar = Scrollbar(leftFrame)
            scrollbar.grid(row = row+3,column=3,sticky=W,pady=10,padx=10)

            for i in range(len(action_log_messages)):

                listbox.insert(END,action_log_messages[i])

            listbox.config(yscrollcommand = scrollbar.set)
            scrollbar.config(command = listbox.yview)
            ###############################################################

            # Now we have to return these updated values for re-rendering -->Pass these to a function
            RenderTissues(colorFunc,alphaChannelFunc ,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow)




def HeartDisplay():
    global action_log_messages
    global listbox
    if file !="":
        global x
        x.destroy()
        volumeMapper,volume,render,renWindow,renWinInteract,colorFunc,alphaChannelFunc,volumeProperty = heart.returnHeartObjects(root)
        v= StringVar() # stores the values of the textBox
        sliderVal = IntVar() # stores the value from the slider variable


        v.set("-999")
        Label(leftFrame,text="Tissue Number: ").grid(row=row,column=0,sticky=W,pady =10)
        ### Choosing a Tissue Number
        Tissue = Entry(leftFrame,textvariable=v,width=5)
        Tissue.grid(row=row,column=1,sticky=W,pady=10,padx=1)

        #Slider for setting opacity
        Label(leftFrame,text="Opacity: ").grid(row=row,column=2,sticky=W,pady = 10, padx =5)
        opacity_slider = Scale(leftFrame, from_=0, to=100, orient=HORIZONTAL)
        opacity_slider.grid(row=row,column=3,sticky=W,pady = 10, padx = 10)
        opacity_slider.set(100)

        ### Choosing the Tissue Colour
        partNumber = int(v.get())
        tissueColor = Button(leftFrame,text="Colour", bg="orange",command= lambda:TissueColor(int(v.get()),opacity_slider.get(),colorFunc,alphaChannelFunc  ,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow))
        tissueColor.grid(row=row,column=4,sticky=W,pady = 10, padx = 10)

        ### row = row + 1
        v1= StringVar() # Sores the value in the delete entry box
        v1.set("-999")

        Label(leftFrame,text="Tissue Number: ").grid(row=row+1,column=0,sticky=W,pady =10)
        delete_part = Entry(leftFrame,textvariable=v1,width=5)
        delete_part.grid(row=row+1,column=1,sticky=W,pady=10,padx=1)

        delete_color = Button(leftFrame,text="Remove Colour",bg="red",command=lambda: DeleteColorFunction(int(v1.get()),colorFunc,alphaChannelFunc ,volumeProperty,volumeMapper,render,volume,renWinInteract,renWindow))
        delete_color.grid(row=row+1,column=2,sticky=W,pady=10,padx=10)

        ## A list of the actions performed :: Action Logs
        Label(leftFrame,text="Action Logs",fg="black",bg="orange").grid(row = row+2,column=0,sticky=W,pady=10,padx=10)
        scrollbar = Scrollbar(leftFrame)
        scrollbar.grid(row = row+3,column=3,sticky=W,pady=10,padx=10)

        listbox = Text(leftFrame,height=10,width=45)
        listbox.grid(row = row+3,columnspan=3,sticky=W,pady=10,padx=10)

        for i in range(len(action_log_messages)):

            listbox.insert(END,action_log_messages[i])

        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)

        volumeProperty.SetScalarOpacity(alphaChannelFunc)
        volumeProperty.SetColor(colorFunc)
        volumeProperty.ShadeOn()

        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)
        render.AddVolume(volume)
        render.ResetCamera()

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
