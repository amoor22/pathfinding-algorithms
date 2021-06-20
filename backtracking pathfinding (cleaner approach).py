maze = [
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]


def solve(maz, pos, end):
    row, col = pos
    if pos == end:
        maz[row][col] = '#'
        return True
    if maz[row][col] == 1:
        maz[row][col] = '#'
        if col < len(maz[0]) - 1:
            if solve(maz, [row, col + 1], end):
                return True
        if row < len(maz) - 1:
            if solve(maz, [row + 1, col], end):
                return True
        maz[row][col] = 0
    return False
solve(maze, [0, 0], [3, 3])
for i in maze:
    print(*i)