import numpy as np

def cellOrdering(cell1, cell2, direction):
    return np.dot((cell1.pos - cell2.pos), direction)

class Cell:
    def __init__(self, vertices):
        self.vertices = vertices
        self.pos = sum(vertices) / len(vertices)
        self.neighbours = []
        self.generation = None
        self.predecessors = []
        self.successors = []

    def __repr__(self):
        return str(len(self.neighbours))

    def addNeighbour(self, cell):
        self.neighbours.append(cell)

    def findOrder(self, direction):
        self.predecessors = []
        self.successors = []
        for neighbour in self.neighbours:
            order = cellOrdering(self, neighbour, direction) 
            if order > 0:
                self.predecessors.append(neighbour)
            elif order < 0:
                self.successors.append(neighbour)
