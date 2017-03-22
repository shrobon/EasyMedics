import vtk
dir_ = r"CT1/CT"

# Read data
reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dir_)
reader.Update()

# Create colour transfer function
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
colorFunc.AddRGBPoint(-77, 0.54902, 0.25098, 0.14902)
colorFunc.AddRGBPoint(94, 0.882353, 0.603922, 0.290196)
colorFunc.AddRGBPoint(179, 1, 0.937033, 0.954531)
colorFunc.AddRGBPoint(260, 0.615686, 0, 0)
colorFunc.AddRGBPoint(3071, 0.827451, 0.658824, 1)

# Create opacity transfer function
alphaChannelFunc = vtk.vtkPiecewiseFunction()
alphaChannelFunc.AddPoint(-3024, 0.0)
alphaChannelFunc.AddPoint(-77, 0.0)
alphaChannelFunc.AddPoint(94, 0.29)
alphaChannelFunc.AddPoint(179, 0.55)
alphaChannelFunc.AddPoint(260, 0.84)
alphaChannelFunc.AddPoint(3071, 0.875)

# Instantiate necessary classes and create VTK pipeline
volume = vtk.vtkVolume()
ren = vtk.vtkRenderer()
#Setting the viewport of the heart renderer 
ren.SetViewport(0,0,0.6,1)
ren.SetBackground(0.1,0.2,0.4)

#renderer2
ren2 = vtk.vtkRenderer()
ren2.SetViewport(0.6,0.5,1,1)
ren2.SetBackground(0,0,0)

#renderer3 ## Problem with viewport Position
ren3 = vtk.vtkRenderer()
ren3.SetViewport(0.6,0,1,0.5)
ren3.SetBackground(0,0,0)


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.AddRenderer(ren2)
renWin.AddRenderer(ren3)

iren = vtk.vtkRenderWindowInteractor()
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
iren.SetRenderWindow(renWin)
renWin.SetSize(800,800)
iren.Initialize()



#defining the image plane widget 
RGB_tuples = [(1, 0, 0), (0, 1, 0), (0, 0, 1)] # define colors for plane outline  

# Define look up table for displaying the data
table = vtk.vtkLookupTable()
table.SetRange(-1000, 3072)
table.SetRampToLinear()
table.SetValueRange(0, 1)
table.SetHueRange(0.0, 1.0)
table.SetSaturationRange(0.0, 0.0)

mapToColors = vtk.vtkImageMapToColors()
mapToColors.SetInputConnection(reader.GetOutputPort())
mapToColors.SetLookupTable(table)
mapToColors.Update()

# A picker is used to get information about the volume
picker = vtk.vtkCellPicker()
picker.SetTolerance(0.005)


# Define plane widgets for x, y and z
planeWidgetX= vtk.vtkImagePlaneWidget() 

# Set plane properties
planeWidgetX.SetInput(mapToColors.GetOutput())
planeWidgetX.SetPlaneOrientationToXAxes()     
planeWidgetX.DisplayTextOn()
planeWidgetX.SetSliceIndex(100)
planeWidgetX.SetPicker(picker)
planeWidgetX.SetLookupTable(table)
planeWidgetX.SetColorMap(mapToColors)
planeWidgetX.SetKeyPressActivationValue("x")
planeWidgetX.GetPlaneProperty().SetColor(RGB_tuples[0])
    
# Place plane widget and set interactor
planeWidgetX.SetCurrentRenderer(ren)
planeWidgetX.SetInteractor(iren)
planeWidgetX.PlaceWidget()
planeWidgetX.On() 

# Code for getting the sliced portion of the plane
slicedImage = planeWidgetX.GetResliceOutput()
actor = vtk.vtkImageActor()
actor.GetMapper().SetInput(slicedImage)
############################################	

################################
## For the Histogram Plotting ##
################################
#components=imageDataGeometryFilter.GetOutput().GetNumberOfScalarComponents()
#print components

plot = vtk.vtkXYPlotActor()
plot.SetLabelFormat( "%g" )
plot.SetXTitle( "Pixel Intensity " )
plot.SetYTitle( "Frequency" )
plot.SetXValuesToValue()
extract = vtk.vtkImageExtractComponents()
extract.SetInput(slicedImage)
extract.SetComponents( 0 )

histogram = vtk.vtkImageAccumulate()
(x,y)=reader.GetOutput().GetScalarRange()
print x
print y 

#histogram.SetComponentExtent()
histogram.SetComponentExtent(int(x),int(y),0,0,0,0);
histogram.SetComponentOrigin(0,0,0);
histogram.SetComponentSpacing(1,1,1);
histogram.IgnoreZeroOn();
histogram.SetInput(extract.GetOutput())
histogram.Update()

plot.SetXRange( x, y );
#plot.SetYRange( 0, y );
plot.AddInput(histogram.GetOutput())
#################################


# Define volume mapper
volumeMapper = vtk.vtkSmartVolumeMapper()  
volumeMapper.SetInput(reader.GetOutput())

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
ren2.AddActor(actor)
ren2.ResetCamera()

ren3.AddActor(plot)
ren3.ResetCamera()

# Render the scene
renWin.Render()
iren.Start()