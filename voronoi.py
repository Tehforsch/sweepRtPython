from scipy.spatial import Voronoi
import numpy as np
from cell import Cell
from grid import Grid

def getVoronoiGrid(points, xRange, yRange):
    voronoiGrid = Voronoi(points)
    cells = []
    regions = [r for r in voronoiGrid.regions if r != [] and not -1 in r]
    for region in regions:
        vertices = getVertices(voronoiGrid, region, xRange, yRange)
        cells.append(Cell(vertices))
    grid = Grid(cells)
    for (i, region1) in enumerate(regions):
        for (j, region2) in enumerate(regions):
            if j <= i: 
                continue
            intersection =  set(region1).intersection(set(region2))
            intersection.discard(-1)
            if len(intersection) > 0:
                grid.connect(cells[i], cells[j])
    return grid

def getVertices(voronoiGrid, region, xRange, yRange):
    vertices = []
    center = sum(voronoiGrid.vertices[i] for i in region if i != -1)
    for i in region:
        if i != -1:
            vertices.append(voronoiGrid.vertices[i])
        else:
            vertices.append(closestCorner(center, xRange, yRange))
    return vertices

def closestCorner(pos, xRange, yRange):
    x = snap(pos[0], xRange[0], xRange[1])
    y = snap(pos[1], yRange[0], yRange[1])
    return np.array([x, y])

def snap(value, minValue, maxValue):
    if value < (minValue + maxValue) / 2:
        return minValue
    else:
        return maxValue

