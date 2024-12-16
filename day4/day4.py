def isMatch(row, col, wordIndex, arr, word, dir):
    if wordIndex == len(word):
        return True
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return False
    return arr[row][col] == word[wordIndex] and isMatch(row+dir[0], col+dir[1], wordIndex+1, arr, word, dir)


def findWord(arr, word):
    # part 1
    count = 0
    dirGrid = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == j == 0:
                continue
            dirGrid.append([i,j])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for dir in dirGrid:
                if isMatch(i,j,wordIndex=0, arr=arr, word=word, dir=dir):
                    print(i,j, dir)
                    count += 1
    return count

def checkOutOfBounds(row, col, arr):
    return row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0])

def isMatchXMAS(row, col, arr, dir):
    if arr[row][col] == "A":
        if checkOutOfBounds(row+dir[0], col+dir[1], arr) or checkOutOfBounds(row-dir[0], col-dir[1], arr):
            return False
        return arr[row+dir[0]][col+dir[1]] == "M" and arr[row-dir[0]][col-dir[1]] == "S"
    else:
        return False

def checkIsMatchDiagonal(row, col, arr, dir, sign, word, wordIndex):
    if wordIndex < 0 or wordIndex == len(word):
        return True
    if checkOutOfBounds(row, col, arr):
        return False
    return arr[row][col] == word[wordIndex] and checkIsMatchDiagonal(row+sign*dir[0], col+sign*dir[1],arr,dir,sign,word,wordIndex+sign)

def isMatchXMASGeneral(row, col, arr, dir, word):
    middleIndex = len(word)//2
    if arr[row][col] == word[middleIndex]:
        return checkIsMatchDiagonal(row, col, arr, dir, -1, word, middleIndex-1) and checkIsMatchDiagonal(row, col, arr, dir, 1, word, middleIndex+1)
    else:
        return False

def findXMAS(arr):
    # part 2
    count = 0
    dirGrid = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 or j == 0:
                continue
            dirGrid.append([i,j])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            dirMatchCount = 0
            for dir in dirGrid:
                # if isMatchXMASGeneral(i,j, arr, dir, "MAS"):
                #     dirMatchCount += 1
                if isMatchXMAS(i,j,arr,dir):
                    dirMatchCount += 1
                    
            if dirMatchCount == 2:
                count += 1
    return count

def run():
    with open("input.txt", "r") as f:
        wordSearchList = [x.strip("\n") for x in f.readlines()]
    wordSearchArrary = []
    for row in wordSearchList:
        rowLst = []
        for char in row:
            rowLst.append(char)
        wordSearchArrary.append(rowLst)
    
        
    return findXMAS(wordSearchArrary)
print(run())