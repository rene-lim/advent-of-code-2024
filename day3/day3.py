import re

                    
def findMatch(txt):
    # part 1
    res = 0
    matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", txt)
    for m in matches:
        first, second = m.group().split(",")
        first = int(first.strip("mul("))
        second = int(second.strip(")"))
        res += first*second
    return res

def splitDosFromDonts(txt):
    # part 2
    dos = txt.split("do()")
    res = 0
    for do in dos:
        res += findMatch(do.split("don't()")[0])
    return res

def run():
    with open("input.txt", "r") as f:
        txt = f.read()
    return splitDosFromDonts(txt)

print(run())