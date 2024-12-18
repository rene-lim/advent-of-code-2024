
def isOutOfBounds(row, col, grid):
    return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])

def startTrail(row,col,grid,prev):
    # print("a", row, col)
    if isOutOfBounds(row, col, grid):
        return {(-1,-1)}
    if (grid[row][col] - prev) != 1:
        return {(-1,-1)}
    if grid[row][col] == 9:
        return {(row, col)}
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    allowedTrails = set()
    for dir in dirs:
        allowedTrails.update(startTrail(row+dir[0], col+dir[1], grid, grid[row][col]))
    return allowedTrails

def part1(grid):
    allowedTrails = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                allowedTrails += len(list(filter(lambda x: not isOutOfBounds(x[0],x[1], grid),startTrail(i,j,grid, -1))))
                print("b", allowedTrails)
    return allowedTrails


def startTrail2(row,col,grid,prev):
    # print("a", row, col)
    if isOutOfBounds(row, col, grid):
        return 0
    if (grid[row][col] - prev) != 1:
        return 0
    if grid[row][col] == 9:
        return 1
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    allowedTrails = 0
    for dir in dirs:
        allowedTrails += startTrail2(row+dir[0], col+dir[1], grid, grid[row][col])
    return allowedTrails

def part2(grid):
    allowedTrails = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                allowedTrails += startTrail2(i,j,grid, -1)
                print("b", allowedTrails)
    return allowedTrails

def run():
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            grid.append([int(x) for x in line.strip('\n')])
            
    return part1(grid)

print(run())


