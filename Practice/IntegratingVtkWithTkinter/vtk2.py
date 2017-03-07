#__Author__ : Shrobon
#__Description__ : CubeSource example with Tkinter --> Just for testing purpose
from __future__ import division
from Tkinter import *
import sys
import vtk


from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor
import vtk.tk.vtkTkRenderWidget



#val = 0.0
root = Tk()

#Function for accessing the slider values
def show_values(event):
    val = float("{0:.2f}".format(slider.get()/255))
    label.config(text=str(val))
    
    
#For naming the title bar
root.title("Hello From Tkinter")
frame = Frame(root)
frame.pack(side='top')


#Button(root,text="Show").pack()
label = Label(root,fg='blue')
label.pack()


cube = vtk.vtkCubeSource()
cube.Modified()
mapper = vtk.vtkPolyDataMapper()
actor = vtk.vtkActor()


mapper.SetInputConnection(cube.GetOutputPort())
actor.SetMapper(mapper)
#
render = vtk.vtkRenderer()
#render.SetBackground(val,val,val)
render.AddActor(actor)


renWindow = vtk.vtkRenderWindow()
renWindow.AddRenderer(render)

renWinInteract = vtkTkRenderWindowInteractor(root,rw=renWindow, width=400, height=400)                   
renWinInteract.Initialize()
renWinInteract.pack(side='top', fill='both', expand=1)


def change_background(num):
    val = float("{0:.2f}".format(slider.get()/255))
    label.config(text=str(val))
    #render.SetBackground(val,val,val)
    actor.GetProperty().SetColor(val,0,val)
    renWindow.Render()

#Slider to change the background colour of the renderer
slider = Scale(root,from_=0, to_=255, orient = HORIZONTAL,command=change_background,label="BG_COL")
#slider = Scale(root,from_=0, to_=255, orient = HORIZONTAL)
slider.set(0)
slider.pack()






renWinInteract.Start()
root.mainloop()
