import vtk
dataset_directory = r"../Examples/CT"
# Read data
reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dataset_directory)
reader.Update()



volume = vtk.vtkVolume()
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
renWin.SetSize(800,800)

# Define volume mapper
volumeMapper = vtk.vtkSmartVolumeMapper()  
volumeMapper.SetInputConnection(reader.GetOutputPort())

# Define volume properties
volumeProperty = vtk.vtkVolumeProperty()
#volumeProperty.SetScalarOpacity(alphaChannelFunc)
#volumeProperty.SetColor(colorFunc)
volumeProperty.ShadeOn()

# Set the mapper and volume properties
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)  

# Add the volume to the renderer
ren.AddVolume(volume)

# Render the scene
renWin.Render()
iren.Start()