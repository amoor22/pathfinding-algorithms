import queue


def createMaze():
    maze = []
    maze.append(['#', '#', '#', '#', 'o', '#', '#', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', '#', '#', 'x', '#', '#', '#', '#'])
    return maze


def createMaze2():
    maze = []
    maze.append(['#', '#', '#', '#', 'o', '#', '#', '#'])
    maze.append(['#', ' ', ' ', '#', ' ', ' ', ' ', '#'])
    maze.append(['#', ' ', ' ', '#', '#', '#', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', '#', '#', 'x', '#', '#', '#', '#'])
    return maze


def printMaze(maze):
    for i in maze:
        print(*i)


def valid(maze, path, start=None):
    if start is None:
        start = [0, 4]
    possible = True
    done = False
    for j in path:
        if j == 'r':
            if maze[start[0]][start[1] + 1] == 'x':
                done = True
            if maze[start[0]][start[1] + 1] == ' ' and start[1] < len(maze[0]) - 1 or maze[start[0]][start[1] + 1] == 'x':
                start[1] += 1
            else:
                possible = False
        if j == 'l':
            if maze[start[0]][start[1] - 1] == 'x':
                done = True
            if maze[start[0]][start[1] - 1] == ' ' and start[1] > 0 or maze[start[0]][start[1] - 1] == 'x':
                start[1] -= 1
            else:
                possible = False

        if j == 'u':
            if maze[start[0] - 1][start[1]] == 'x':
                done = True
            if maze[start[0] - 1][start[1]] == ' ' and start[0] > 0 or maze[start[0] - 1][start[1]] == 'x':
                start[0] -= 1
            else:
                possible = False

        if j == 'd':
            if maze[start[0] + 1][start[1]] == 'x':
                done = True
            if maze[start[0] + 1][start[1]] == ' ' and start[0] < len(maze) - 1 or maze[start[0] + 1][start[1]] == 'x':
                start[0] += 1
            else:
                possible = False
    return (possible, done)


def solve(maze):
    que = queue.Queue()
    que.put('')
    found = False
    while not found:
        last = que.get()
        for a in ['r', 'l', 'u', 'd']:
            add = last + a
            if valid(maze, add)[0]:
                que.put(add)
            if valid(maze, add)[1]:
                found = True
                return add



def mover(maze, actions, pos):
    row, col = pos
    for x in actions:
        if x == 'r':
            maze[row][col + 1] = 'o'
            col += 1
        elif x == 'l':
            maze[row][col - 1] = 'o'
            col -= 1
        elif x == 'u':
            maze[row - 1][col] = 'o'
            row -= 1
        elif x == 'd':
            maze[row + 1][col] = 'o'
            row += 1


new_maze = createMaze2()
printMaze(new_maze)
print('Shortest solution: ',solve(new_maze))
mover(new_maze, solve(new_maze), [0, 4])
printMaze(new_maze)
