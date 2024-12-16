import copy

def hasExitedGrid(row, col, grid):
    return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])

def nextStep(i, j, currDir):
    return i + currDir[0], j + currDir[1]

def trackPath(grid, currPosition):
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    i, j = currPosition
    count = 0
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    numRightTurns = 0
    while True:
        if not visited[i][j]:
            count += 1
        visited[i][j] = True
        currDir =  dir[numRightTurns%len(dir)]
        nextRow, nextCol = nextStep(i, j, currDir)
        if hasExitedGrid(nextRow, nextCol, grid):
            break
        print("a", nextRow, nextCol)
        if grid[nextRow][nextCol] == "#":
            numRightTurns += 1
        else:
            i, j = nextStep(i, j, currDir)
    return count

def trackPathWithDirection(grid, currPosition):
    
    visited = [[[] for j in range(len(grid[0]))] for i in range(len(grid))]
    i, j = currPosition
    count = 0
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    numRightTurns = 0
    while True:
        if not visited[i][j]:
            count += 1
        currDir =  dir[numRightTurns%len(dir)]
        if currDir in visited[i][j]:
            return True
        visited[i][j].append(currDir)
        nextRow, nextCol = nextStep(i, j, currDir)
        if hasExitedGrid(nextRow, nextCol, grid):
            break
        if grid[nextRow][nextCol] == "#":
            numRightTurns += 1
        else:
            i, j = nextStep(i, j, currDir)
    return False

def trackPath2(grid, currPosition):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            gridCopy = copy.deepcopy(grid)
            if gridCopy[i][j] != "#":
                gridCopy[i][j] = "#"
                print("a", i, j, count)
                if trackPathWithDirection(gridCopy, currPosition):
                    count += 1
    return count

def run():
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip("\n")))
    currPosition = [0,0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                currPosition = [i,j]
    
    return trackPath2(grid,currPosition)

print(run())