from maze import Maze
# to track the present co-ordinate and it's cost
class Tracer:
    def __init__(self, pos: Maze, cost, path = list()):
        self.pos = pos
        self.cost = cost
        self.path = path