import vtk
dataset_directory = r"..\Examples\CT"
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


# Create colour transfer function
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(1, 0.0, 0.0, 0.0)
colorFunc.AddRGBPoint(2, 0.54902, 0.25098, 0.14902)
colorFunc.AddRGBPoint(3, 0.882353, 0.603922, 0.290196)
colorFunc.AddRGBPoint(4, 1, 0.937033, 0.954531)
colorFunc.AddRGBPoint(5, 0.615686, 0, 0)
#colorFunc.AddRGBPoint(6, 0.827451, 0.658824, 1)

alphaChannelFunc = vtk.vtkPiecewiseFunction()
alphaChannelFunc.AddPoint(1, 0.0)
alphaChannelFunc.AddPoint(2, 0.0)
alphaChannelFunc.AddPoint(3, 0.29)
alphaChannelFunc.AddPoint(4, 0.55)
alphaChannelFunc.AddPoint(5, 0.84)
#alphaChannelFunc.AddPoint(6, 0.875)

# Define volume properties
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetScalarOpacity(alphaChannelFunc)
volumeProperty.SetColor(colorFunc)
volumeProperty.ShadeOn()

# Set the mapper and volume properties
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)  

# Add the volume to the renderer
ren.AddVolume(volume)

# Render the scene
renWin.Render()
iren.Start()