import sys
from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor
from tkFileDialog import *
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

def WriteAsJPEG(filename,rendering_window):

    ##### Section for the JPEG Writer ####################
    win2img = vtk.vtkWindowToImageFilter()
    win2img.SetInput(rendering_window)
    #win2img.SetMagnification(2)
    win2img.Update()

    jpegWriter = vtk.vtkJPEGWriter()
    jpegWriter.SetFileName(filename)
    jpegWriter.SetInputConnection(win2img.GetOutputPort())
    jpegWriter.Write()

