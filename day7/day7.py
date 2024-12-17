import copy

def isHitTarget(target, values, currNum):
    if currNum == target:
        return True
    if not values:
        return False
    operators = [lambda x,y: x+y, lambda x,y: x*y]
    isHit = False
    for op in operators:
        copyLst = copy.deepcopy(values)
        num = copyLst.pop(0)
        isHit = isHit or isHitTarget(target, copyLst, op(currNum, num))
    return isHit

def part1(arr):
    count = 0
    for target, values in arr:
        firstNum = values.pop(0)
        if isHitTarget(target, values, firstNum):
            count += target
    return count

def getNumDigits(num):
    count = 1
    while num//10>0:
        count += 1
        num //= 10
    return count

def getFullNumber(x,y):
    return (x or 0)*10**getNumDigits(y)+y

def isHitTarget2(target, values, currNum):
    if currNum == target and not values:
        return True
    if not values:
        return False
    operators = [lambda x,y: (x or 0)+y, lambda x,y: (x or 1)*y, getFullNumber]
    isHit = False
    for op in operators:
        copyLst = copy.deepcopy(values)
        num = copyLst.pop(0)
        isHit = isHit or isHitTarget2(target, copyLst, op(currNum, num))
        if isHit:
            return True
            
    return isHit

def part2(arr):
    count = 0
    res = 0
    for target, values in arr:
        res += 1
        print(res)
        if isHitTarget2(target, values, None):
            count += target
    return count
        

def run():
    arr = []
    with open("input.txt", "r") as f:
        for line in f:
            target, nums  = line.split(":")
            arr.append([int(target), [int(x) for x in nums.strip().split(" ")]])
    return part2(arr)

print(run())
