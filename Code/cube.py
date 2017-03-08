import vtk
from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor

def returnCubeObjects(root):
    
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

    renWinInteract = vtkTkRenderWindowInteractor(root,rw=renWindow, width=800, height=800) 
    return actor,render,renWindow,renWinInteract