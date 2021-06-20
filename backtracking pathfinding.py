maze = [
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
]

path = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
def find_path(path, maze, row, col, endpoint):
    if [row, col] == endpoint:
        path[row][col] = 1
        return True
    if maze[row][col] == 1:  # if it's empty
        path[row][col] = 1   # go there
        # if you can go right continue
        if find_path(path, maze, row, col + 1, endpoint):
            return True
        # if you can go down continue
        if find_path(path, maze, row + 1, col, endpoint):
            return True
        # if neither return true then backtrack and unwind
        path[row][col] = 0
    # (return False if there are no possible movements in the current position)
    return False


find_path(path, maze, 0, 0, [3,3])

for i in path:
    print(*i)
print()
for row in range(len(path)):
    for col in range(len(path[0])):
        if path[row][col] == 1:
            print([row, col], end=' ')