def numbersSmallerThan(smaller, ruleDict, visited):
    lst = []
    if ruleDict.get(smaller):
        # print("a", smaller, ruleDict.get(smaller), visited)
        for i in ruleDict.get(smaller):
            lst.append(i)
            if smaller not in visited:
                visited.append(smaller)
                lst.extend(numbersSmallerThan(i, ruleDict, visited))
    return lst

def checkRule(ruleDict, update):
    print("b", update, len(update))
    for i in range(len(update)-1, 0, -1):
        print("c", i, update[i], ruleDict[update[i]])
        biggerNumbersCurr = set(update[:i])
        biggerNumbersAll = set(ruleDict[update[i]])
        # biggerNumbersAll = set(numbersSmallerThan(update[i], ruleDict, []))
        if biggerNumbersAll.intersection(biggerNumbersCurr):
            print(biggerNumbersCurr, biggerNumbersAll, biggerNumbersAll.intersection(biggerNumbersCurr))
            print()
            return False
    return True

def checkRuleAndAlter(ruleDict, update):
    print("b", update, len(update))
    isAltered = False
    for i in range(len(update)-1, -1, -1):
        if update[i] not in ruleDict:
            continue
        # print("c", i, update[i], ruleDict[update[i]])
        biggerNumbersCurr = set(update[:i])
        biggerNumbersAll = set(ruleDict[update[i]])
        wrongNumbers = biggerNumbersAll.intersection(biggerNumbersCurr)
        if wrongNumbers:
            isAltered = True
            print("d", biggerNumbersCurr, biggerNumbersAll, wrongNumbers)
            _, correctedNumbers = checkRuleAndAlter(ruleDict, list(wrongNumbers))
            for num in correctedNumbers:
                update.pop(update.index(num))
                update.insert(i, num)
            print("f", update)
    print()
    return isAltered, update


def run():
    with open("input.txt", "r") as f:
        ruleDict = {}
        updates = []
        for line in f:
            line = line.strip("\n")
            if "|" in line:
                first, second = [int(x) for x in line.split("|")]
                if first in ruleDict:
                    currList = ruleDict[first]
                    currList.append(second)
                    ruleDict[first] = currList
                else:
                    ruleDict[first] = [second]
            elif "," in line:
                updates.append([int(x) for x in line.split(",")])
    total = 0
    for update in updates:
        # if checkRule(ruleDict, update):
        #     total += update[len(update)//2]
        isAltered, update = checkRuleAndAlter(ruleDict, update)
        if isAltered:
            total += update[len(update)//2]
    return total

print(run())