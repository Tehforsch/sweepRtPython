import numpy as np

def cellOrdering(cell1, cell2, direction):
    return np.dot((cell1.pos - cell2.pos), direction) / np.linalg.norm(cell1.pos - cell2.pos)

class Cell:
    def __init__(self, vertices):
        self.vertices = vertices
        self.pos = np.sum(vertices, axis=0) / len(vertices)
        self.neighbours = []
        self.generation = None
        self.predecessors = []
        self.successors = []
        self.domain = 2 * (1 if self.pos[0] < 0.4 else 0) + 1 * (1 if self.pos[1] < 0.4 else 0)

    def __repr__(self):
        return str(len(self.neighbours))

    def addNeighbour(self, cell):
        self.neighbours.append(cell)

    def findOrder(self, direction):
        self.predecessors = []
        self.successors = []
        for neighbour in self.neighbours:
            order = cellOrdering(self, neighbour, direction) 
            if order > 0.5:
                self.predecessors.append(neighbour)
            elif order < -0.5:
                self.successors.append(neighbour)

    def __repr__(self):
        return "{}".format(self.name)

