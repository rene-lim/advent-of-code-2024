def generateDiskMap(s):
    diskMapCount = 0
    diskMap = []
    for index, char in enumerate(s):
        numRepeat = int(char)
        elem = "."
        if index%2==0:
            elem = diskMapCount
            diskMapCount += 1
        for i in range(numRepeat):
            diskMap.append(elem)
    return diskMap

def getLastElem(diskMap):
    elem = diskMap.pop()
    while elem == ".":
        elem = diskMap.pop()
    return elem

def freespace(diskMap):
    for index, elem in enumerate(diskMap):
        if index == len(diskMap):
            break
        if elem == ".":
            diskMap[index] = getLastElem(diskMap)
    return diskMap

def calculateCheckSum(diskMap):
    sm = 0
    for index, elem in enumerate(diskMap):
        sm += index * elem
    return sm

def part1(s):
    diskMap = generateDiskMap(s)
    diskMap = freespace(diskMap)
    checkSum = calculateCheckSum(diskMap)
    return checkSum

def generateDiskMap2(s):
    diskMapCount = 0
    diskMap = []
    for index, char in enumerate(s):
        numRepeat = int(char)
        elem = "."
        if index%2==0:
            elem = diskMapCount
            diskMapCount += 1
        if numRepeat > 0:
            diskMap.append((elem, numRepeat))
    return diskMap

def findAndReplace(diskMap, elem, numRepeat, index):
    decrease = 0
    for i, e in enumerate(diskMap):
        currElem, currRepeat = e
        if currElem == "." and currRepeat >= numRepeat and index > i:
            repeatsLeft = currRepeat - numRepeat
            print('before', index, i, elem, numRepeat, diskMap)
            diskMap.pop(index)
            diskMap.insert(index,(".", numRepeat))
            diskMap.pop(i)
            if repeatsLeft > 0:
                decrease = 1
                diskMap.insert(i, (".", repeatsLeft))
            diskMap.insert(i, (elem, numRepeat))
            print('after', index, i, elem, numRepeat, diskMap)
            return decrease
    return decrease

def freespace2(diskMap):
    i = len(diskMap) - 1
    while i >= 0:
        elem, numRepeat = diskMap[i]
        if elem != ".":
            print("d", elem, numRepeat, i)
            i += findAndReplace(diskMap, elem, numRepeat, i)
        i -= 1
    return diskMap
            
def calculateCheckSum2(diskMap):
    count = 0
    sm = 0
    for e, numRepeats in diskMap:
        # print("f", count, e, numRepeats, sm)
        for i in range(numRepeats):
            if e != ".":
                sm += count*e
            count += 1
    return sm

def part2(s):
    diskMap = generateDiskMap2(s)
    diskMap = freespace2(diskMap)
    checkSum = calculateCheckSum2(diskMap)
    return checkSum

def run():
    s = ""
    with open("input.txt", "r") as f:
        for line in f:
            s += line.strip("\n")
    return part2(s)

print(run())