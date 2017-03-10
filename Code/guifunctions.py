from __future__ import division
import sys
from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor
from tkFileDialog import *
from tkMessageBox import *
from tkColorChooser import askcolor
import vtk


def OpenFile():
    # To open a file
    global file 
    file = askopenfilename()
    print file
    #To flush out the print output buffers
    sys.stdout.flush() 


def OpenFolder():
    # To open a direcotry
    global directory
    directory = askdirectory(initialdir='.')
    print directory
    sys.stdout.flush()

def SaveOutput(renWindow):
    global saveFileName
    saveFileName = asksaveasfilename()
    print saveFileName
    sys.stdout.flush()
    WriteAsJPEG(saveFileName,renWindow)

def WriteAsJPEG(filename,renderingWindow):

    ##### Section for the JPEG Writer ####################
    win2img = vtk.vtkWindowToImageFilter()
    win2img.SetInput(renderingWindow)
    #win2img.SetMagnification(2)
    win2img.Update()

    jpegWriter = vtk.vtkJPEGWriter()
    jpegWriter.SetFileName(filename)
    jpegWriter.SetInputConnection(win2img.GetOutputPort())
    jpegWriter.Write()

def Quit(root):
    answer = askquestion("Quit","Are you Sure ? Please Save your work",icon='warning')
    if answer == 'yes':
        root.quit()
    else:
        pass


def BgColor(render,renWindow):
    #user input to choose color of background
    color = askcolor(color="#6B7722",title="Background Color")
    #fetching the rgb color tuple and mapping it in range 0-1
    color = color[0]
    (r,g,b) = color # RGB tuple 
    r = float("{0:.2f}".format(r/255))
    g = float("{0:.2f}".format(g/255))
    b = float("{0:.2f}".format(b/255))
    print r 
    sys.stdout.flush()

    # changing color of background
    render.SetBackground(r,g,b)
    renWindow.Render()
    print color
    sys.stdout.flush()

def FgColor(actor,renWindow):
    #user input to choose color of background
    color = askcolor(color="#6B7722",title="Foreground Color")
    #fetching the rgb color tuple and mapping it in range 0-1
    color = color[0]
    (r,g,b) = color # RGB tuple 
    r = float("{0:.2f}".format(r/255))
    g = float("{0:.2f}".format(g/255))
    b = float("{0:.2f}".format(b/255))


    # changing color of background
    actor.GetProperty().SetColor(r,g,b)
    renWindow.Render()
    print color
    sys.stdout.flush()



