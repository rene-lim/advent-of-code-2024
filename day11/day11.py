def blink(stoneArrangement):
    for i in range(len(stoneArrangement)-1,-1,-1):
        elem = stoneArrangement[i]
        if elem == 0:
            stoneArrangement[i] = 1
        elif len(str(elem))%2 == 0:
            e = str(elem)
            mid = int(len(e)//2)
            # print("a,",e,mid,e[:mid], e[mid:])
            stoneArrangement.pop(i)
            stoneArrangement.insert(i,int(e[mid:].lstrip("0") or 0))
            stoneArrangement.insert(i, int(e[:mid]))
        else:
            stoneArrangement[i] *=2024
    return stoneArrangement

def part1(stoneArrangement):
    for i in range(75):
        print(i, stoneArrangement)
        blink(stoneArrangement)
    return len(stoneArrangement)

def cache(f):
    d = {}
    def cacheDecorator(*args):
        if args in d:
            return d[args]
        d[args] = f(*args)
        return d[args]
    return cacheDecorator

@cache
def blink(stone, count):
    if count == 0:
        return 1
    if stone == 0:
        return blink(1, count-1)
    if len(str(stone))%2 == 0:
        e = str(stone)
        mid = int(len(e)//2)
        return blink(int(e[:mid]),count-1) + blink(int(e[mid:]), count-1)
    return blink(stone*2024, count-1)
    

def part2(stoneArrangement):
    return sum([blink(stone, 75) for stone in stoneArrangement])
        
        

def run():
    stoneArrangement = []
    with open("input.txt", "r") as f:
        for line in f:
            stoneArrangement.extend([int(x) for x in line.strip("\n").split(" ")])
            
    return part2(stoneArrangement)

print(run())