import math
import sys
# g cost is the distance of the path meaning it changes as we go through the nodes
# current node g cost + previous node g cost = g
# object_array = np.empty((7,7), dtype=object)
# object_array[:, :] = node()

class node:
    def __init__(self):
        self.parent = None
        self.index = []
        self.fcost = sys.maxsize
        self.gcost = 0
    def find_neighbors(self, maze, pos):
        row, col = pos
        neighbors = []
        # check right
        if maze[row][col + 1] != 0 and col < len(maze[0]) - 1:
            neighbors.append([row, col + 1])
        # check left
        if maze[row][col - 1] != 0 and col > 0:
            neighbors.append([row, col - 1])
        # check up
        if maze[row - 1][col] != 0 and row > 0:
            neighbors.append([row - 1, col])
        # check down
        if maze[row + 1][col] != 0 and row < len(maze) - 1:
            neighbors.append([row + 1, col])
        # check top-right
        if maze[row - 1][col + 1] != 0 and row > 0 and col < len(maze[0]) - 1:
            neighbors.append([row - 1, col + 1])
        # check top-left
        if maze[row - 1][col - 1] != 0 and row > 0 and col > 0:
            neighbors.append([row - 1, col - 1])
        # check bottom-right
        if maze[row + 1][col + 1] != 0 and row < len(maze) - 1 and col < len(maze[0]) - 1:
            neighbors.append([row + 1, col + 1])
        # check bottom-left
        if maze[row + 1][col - 1] != 0 and row < len(maze) - 1 and col > 0:
            neighbors.append([row + 1, col - 1])
        return neighbors

    def g_cost(self, row, col, prev_pos, prevcost):
        srow, scol = prev_pos
        cost = math.hypot(scol - col, srow - row) + prevcost
        self.gcost = cost
        return cost

    def h_cost(self, row, col, end):
        erow, ecol = end
        cost = math.hypot(ecol - col, erow - row)
        return cost

    def f_cost(self, g_cost, h_cost):
        return g_cost + h_cost


def createMaze():
    maze = []
    maze.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    maze.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 0])
    maze.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 0])
    maze.append([0, 1, 1, 1, 0, 0, 1, 3, 1, 0])
    maze.append([0, 1, 1, 1, 1, 0, 1, 1, 1, 0])
    maze.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 0])
    maze.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    return maze


def maze_print(maze):
    for i in maze:
        print(*i)


object_array = [
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()],
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()],
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()],
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()],
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()],
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()],
    [node(), node(), node(), node(), node(), node(), node(), node(), node(), node()]

]


def give_index():
    row, col = 0, 0
    for i in object_array:
        for j in i:
            j.index = [row, col]
            if col == 9:
                row += 1
                col = 0
            else:
                col += 1


give_index()


def solve(maze, start, end):
    done = False
    srow, scol = start
    current_g = 0
    opn = [object_array[srow][scol]]  # f_cost(g_cost(srow, scol, [srow, scol], 0), h_cost(srow, scol, end))
    closed = []
    iterations = 1
    while not done:
        current = sys.maxsize
        nod_lf = None
        for nod in opn:
            if iterations == 1:
                cost = nod.f_cost(nod.g_cost(srow, scol, [srow, scol], 0), nod.h_cost(srow, scol, end))
                iterations += 1
            else:
                cost = nod.fcost
            if cost < current:
                current_g = nod.gcost
                current = cost
                nod_lf = nod
        print(nod_lf.index)
        if nod_lf.index == end:
            print('found')
            break
        opn.remove(nod_lf)
        closed.append(nod_lf)
        for neighbor in nod_lf.find_neighbors(new_maze, nod_lf.index):
            row, col = neighbor
            neig = object_array[row][col]
            if neig in closed:
                continue
            neig.parent = nod_lf
            neig.fcost = neig.f_cost(neig.g_cost(row, col, nod_lf.index, current_g), neig.h_cost(row, col, end))
            if neig not in opn:
                opn.append(neig)


def retrace(object_matrix, start, endpoint):
    moves = []
    row, col = endpoint
    moves.append(endpoint)
    while True:
        if [row, col] == start:
            break
        parent = object_matrix[row][col].parent
        parent_index = parent.index
        row, col = parent_index
        moves.append([row, col])
    return moves


def mover(maze, moves):
    for i in moves:
        row, col = i
        maze[row][col] = '#'
new_maze = createMaze()
solve(new_maze, [5, 2], [1, 8])
mover(new_maze, retrace(object_array, [5, 2], [1, 8]))
maze_print(new_maze)
# g cost, h cost, f cost
# distance from start, distance from end, sum of g cost and h cost
