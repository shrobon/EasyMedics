from Tkinter import *
import sys
import vtk

from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor
import vtk.tk.vtkTkRenderWidget

root = Tk()
root.title("Hello From Tkinter")
frame = Frame(root)
frame.pack(side='top')

cube = vtk.vtkCubeSource()
mapper = vtk.vtkPolyDataMapper()
actor = vtk.vtkActor()


mapper.SetInputConnection(cube.GetOutputPort())
actor.SetMapper(mapper)


render = vtk.vtkRenderer()
render.SetBackground( 0.329412, 0.34902, 0.427451 )
render.AddActor(actor)
#render.ResetCameraClippingRange()

renWindow = vtk.vtkRenderWindow()
renWindow.AddRenderer(render)

renWinInteract = vtkTkRenderWindowInteractor(root,rw=renWindow, width=400, height=400)                   
renWinInteract.Initialize()
renWinInteract.pack(side='top', fill='both', expand=1)
renWinInteract.Start()

renWindow.Render()
root.mainloop()