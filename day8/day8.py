import math

def isOutOfBounds(i,j,maxRow,maxCol):
    return i < 0 or j < 0 or i >= maxRow or j >= maxCol

def calculateDistance(coordinate):
    return math.sqrt(coordinate[0]**2 + coordinate[1]**2)

def getAntinodes(first, second, dir, defRange):
    antinodeSet = set()
    for i in defRange:
        antinode1 = (second[0]+i*dir[0], second[1]+i*dir[1])
        antinode2 = (first[0]-i*dir[0], first[1]-i*dir[1])
        antinodeSet.update({antinode1, antinode2})
    return antinodeSet

def extendAntinodes(dir, maxRow, maxCol):
    diagonal = calculateDistance((maxRow, maxCol))
    dirLen = calculateDistance(dir)
    return int(diagonal//dirLen)

def findAntinodes(coordinates, maxRow, maxCol):
    antinodeSet = set()
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            first = coordinates[i]
            second = coordinates[j]
            dir = (second[0]-first[0], second[1]-first[1])
            part1Range = range(1,2)
            part2Range = range(extendAntinodes(dir, maxRow, maxCol))
            antinodeSet.update(getAntinodes(first, second, dir, part2Range))
    return antinodeSet

def part1(antennas, maxRow, maxCol):
    antinodeSet = set()
    for antenna, coordinates in antennas.items():
        antinodeSet.update(findAntinodes(coordinates, maxRow, maxCol))
    return len(list(filter(lambda x: not isOutOfBounds(x[0],x[1], maxRow, maxCol), antinodeSet)))

def run():
    antennas = {}
    maxCol = None
    with open("input.txt", "r") as f:
        rowCount = 0
        for line in f:
            line = line.strip("\n")
            if not maxCol:
                maxCol = len(line)
            for index, char in enumerate(list(line)):
                if char != ".":
                    if char in antennas:
                        lst = antennas[char]
                        lst.append((rowCount, index))
                        antennas[char] = lst
                    else:
                        antennas[char] = [(rowCount, index)]
            rowCount += 1
    
    return part1(antennas, rowCount, maxCol)

print(run())