import numpy as np
import plot
from cell import Cell

class Domain:
    def __init__(self, xRange, yRange):
        self.xRange = xRange
        self.yRange = yRange

    
class Grid:
    def __init__(self, cells):
        self.cells = cells

    @staticmethod
    def getCartesian(domainSize, numPointsPerDimension):
        xpoints = np.linspace(*domainSize.xRange, numPointsPerDimension+1)
        ypoints = np.linspace(*domainSize.yRange, numPointsPerDimension+1)
        coordinateGrid = np.array(np.meshgrid(xpoints, ypoints))
        cellGrid = [[
            Cell([
                coordinateGrid[:,i, j], 
                coordinateGrid[:,i+1,j], 
                coordinateGrid[:,i+1,j+1], 
                coordinateGrid[:,i, j+1]]
                ) for i in range(numPointsPerDimension)] for j in range(numPointsPerDimension)]
        grid = Grid([cell for cells in cellGrid for cell in cells])
        for i in range(numPointsPerDimension):
            for j in range(numPointsPerDimension):
                if i < numPointsPerDimension-1:
                    grid.connect(cellGrid[i][j], cellGrid[i+1][j])
                if j < numPointsPerDimension-1:
                    grid.connect(cellGrid[i][j], cellGrid[i][j+1])
        return grid

    def connect(self, cell1, cell2):
        cell1.addNeighbour(cell2)
        cell2.addNeighbour(cell1)

    def setGenerations(self, direction):
        for cell in self.cells:
            cell.generation = None
        for cell in self.cells:
            cell.findOrder(direction)
        noPredecessors = [cell for cell in self.cells if len(cell.predecessors) == 0]
        self.findNextGeneration(noPredecessors)

    def findNextGeneration(self, currentCells, generation=0):
        for cell in currentCells:
            cell.generation = generation
            for successor in cell.successors:
                successor.predecessors.remove(cell)
        nextGeneration = set(laterGenerationCell for cell in currentCells for laterGenerationCell in cell.successors if len(laterGenerationCell.predecessors) == 0)
        if len(nextGeneration) != 0:
            self.findNextGeneration(nextGeneration, generation+1)
