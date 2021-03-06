
from vtk import *
 
# The source file
file_name = "heart.vtk"
 
# Read the source file.
reader = vtkStructuredPointsReader()
reader.SetFileName(file_name)
reader.Update() # Needed because of GetScalarRange
output = reader.GetOutput()
#scalar_range = output.GetScalarRange()
geometryFilter = vtkImageDataGeometryFilter()
geometryFilter.SetInputConnection(reader.GetOutputPort())
geometryFilter.Update()

 
# Create the mapper that corresponds the objects of the vtk file
# into graphics elements
mapper = vtkPolyDataMapper()
mapper.SetInput(geometryFilter.GetOutput())
#mapper.SetScalarRange(scalar_range)
 
# Create the Actor
actor = vtkActor()
actor.SetMapper(mapper)
 
# Create the Renderer
renderer = vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1) # Set background to white
 
# Create the RendererWindow
renderer_window = vtkRenderWindow()
renderer_window.AddRenderer(renderer)
 
# Create the RendererWindowInteractor and display the vtk_file
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderer_window)
interactor.Initialize()
interactor.Start()
