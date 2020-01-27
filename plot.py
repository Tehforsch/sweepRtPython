import matplotlib.pyplot as plt

def drawLine(start, end, color="b"):
    plt.plot([start[0], end[0]], [start[1], end[1]], color=color)

def drawArrow(start, end, color="b"):
    plt.arrow(start[0], start[1], end[0]-start[0], end[1]-start[1], color=color, linewidth=1)

def showGrid(domain, grid, filename):
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    maxGeneration = max(cell.generation for cell in grid.cells if cell.generation is not None)
    getColor = lambda cell: plt.cm.winter(cell.generation / maxGeneration) if cell.generation is not None else "r"
    for cell in grid.cells:
        for (v1, v2) in zip(cell.vertices, cell.vertices[1:] + [cell.vertices[0]]):
            drawLine(v1, v2, color=getColor(cell))
        plt.text(cell.pos[0]-0.02, cell.pos[1]-0.02, str(cell.generation))
        for successor in cell.successors:
            p1 = intermediatePoint(cell.pos, successor.pos, 0.2)
            p2 = intermediatePoint(cell.pos, successor.pos, 0.8)
            drawArrow(p1, p2, color="b")
    plt.savefig(filename)
    # plt.show()

def intermediatePoint(start, end, factor):
    return start + (end - start) * factor
