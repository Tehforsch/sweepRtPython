import voronoi
import numpy as np
import tqdm

def cycleCheck(cell, visited):
    for successor in cell.successors:
        if successor in visited:
            print("CYCLE")
        else:
            visited.add(successor)
            cycleCheck(successor, visited)
            visited.remove(successor)
            # cycleCheck(successor, visited + [successor])

def connectedCheck(particles, visited=None, p = None):
    if p is None:
        p = particles[100]
        visited = set()
        wasFirstCall = True
    visited.add(p)
    print(p)
    for p2 in p.successors:
        print(p2)
        connectedCheck(particles, visited)
    if wasFirstCall:
        print(len(visited))

def main():
    dimensions = 3
    direction = np.array([1] + [0] * (dimensions-1))
    for i in tqdm.tqdm(range(100000)):
        grid = voronoi.getVoronoiGrid(np.random.uniform(size=(100, dimensions)), (0, 1), (0, 1))
        for cell in grid.cells:
            cell.findOrder(np.array(direction))
        cycleCheck(grid.cells[0], set([grid.cells[0]]))
        # cycleCheck(grid.cells[0], [grid.cells[0]])

def main2():
    class C(int):
        def __init__(self, x):
            int.__init__(x)
            self.successors = []

        def addSuccessor(self, name):
            self.successors.append(name)

        def __hash__(self):
            return int.__hash__(self)
            
        def __eq__(self, y):
            return int.__eq__(self, y)
            
    with open("out", "r") as f:
        lines = f.readlines()
        particles = set()
        for (x, y) in (line.split(" ") for line in lines):
            particles.add(int(x))
            particles.add(int(y))
        particles = [C(x) for x in particles]
        print(particles)
        for (x, y) in (line.split(" ") for line in lines):
            particles[particles.index(x)].successors.add(particles[particles.index(y)])
            # cX.addSuccessor(cY)
            # print(cX.successors)
        connectedCheck(list(particles))
        p = particles.pop()
        cycleCheck(p, set([p]))

# main()
main2()
