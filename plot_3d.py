import os

os.environ["VTK_USE_OFFSCREEN"] = "1"

import vtk

def create_3d_plot(df):
    points = vtk.vtkPoints()

    # Simulação de trajetória
    for i in range(20):
        points.InsertNextPoint(i, i, i * 2)

    polyData = vtk.vtkPolyData()
    polyData.SetPoints(points)

    vertexFilter = vtk.vtkVertexGlyphFilter()
    vertexFilter.SetInputData(polyData)
    vertexFilter.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(vertexFilter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    interactor.Start()