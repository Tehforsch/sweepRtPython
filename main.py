from grid import Domain, Grid
from voronoi import getVoronoiGrid
import numpy as np
import plot

def showGrid(domain, grid, direction):
    grid.setGenerations(direction)
    # print([c.generation for c in grid.cells])
    plot.showGrid(domain, grid, "pics/grid.png", domainColor=False)
    plot.showGrid(domain, grid, "pics/grid.pdf", domainColor=False)

    # plot.showGrid(domain, grid, "pics/gridNoNumbers.png", domainColor=False)
    plot.showGrid(domain, grid, "pics/gridDomain.png", domainColor=True)

def main():
    np.random.seed(1339)
    domain = Domain((0, 1), (0, 1))
    # g = Grid.getCartesian(domain, 18)
    grid = getVoronoiGrid(np.random.uniform(size=(160, 2)), (0, 1), (0, 1))
    showGrid(domain, grid, [-1, 0])

main()
