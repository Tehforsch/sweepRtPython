import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

def drawLine(start, end, color="b"):
    plt.plot([start[0], end[0]], [start[1], end[1]], color=color)

def drawArrow(start, end, color="r"):
    plt.arrow(start[0], start[1], end[0]-start[0], end[1]-start[1], color=color, linewidth=1, head_width=0.01, length_includes_head=True)

def showGrid(domain, grid, filename, numbers=False, domainColor=False):
    fig, ax = plt.subplots()
    plt.xlim(0.15, 0.85)
    plt.ylim(0.15, 0.65)
    maxGeneration = max(cell.generation for cell in grid.cells if cell.generation is not None)
    n = 5
    getColor = lambda generation: plt.get_cmap("hsv")((generation-n)/(maxGeneration-n))
    print([getColor(i) for i in range(10)])
    patchesPerDomain = [[] for i in range(100)]
    plt.axis("off")
    for cell in grid.cells:
        patchesPerDomain[cell.domain].append(Polygon(cell.vertices))
        # for (v1, v2) in zip(cell.vertices, cell.vertices[1:] + [cell.vertices[0]]):
        #     drawLine(v1, v2, color=getColor(cell))
        if numbers:
            plt.text(cell.pos[0]+0.007, cell.pos[1], str(cell.generation), fontsize=15, horizontalalignment="center", verticalalignment="center")
        for successor in cell.successors:
            p1 = intermediatePoint(cell.pos, successor.pos, False)
            p2 = intermediatePoint(cell.pos, successor.pos, True)
            drawArrow(p1, p2, color=getColor(successor.generation))
    for (i, patchList) in enumerate(patchesPerDomain):
        patches = PatchCollection(patchList)
        if domainColor:
            patches.set_color(getDomainColor(i))
            patches.set_alpha(0.5)
        else:
            patches.set_color(getDomainColor(1))
            patches.set_alpha(0.5)
        ax.add_collection(patches)
    plt.savefig(filename, bbox_inches="tight", dpi=400)

def getDomainColor(i):
    return plt.get_cmap("Set1")(i)

def intermediatePoint(start, end, getFirstPoint):
    length = np.linalg.norm(end-start)
    alpha = 0.012
    if getFirstPoint:
        return end + (start - end) / length * alpha
    else:
        return start + (end - start) / length * alpha
