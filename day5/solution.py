lines = []

# Part 1 & 2
with open("day5/input.txt") as r:
    for line in r.readlines():
        lines.append(line)
movements = []
startMove = False
stacks = []

for Crates in lines:
    if not Crates.replace(" ", "").strip():
        startMove = True
        continue
    if not startMove:
        stacks.append(Crates)
    else:
        movements.append(Crates)

colums = [[line[x] for line in stacks] for x in range(len(stacks[0]))]
columsFormated = []

for a in colums:
    if a[-1].strip():
        a = [b for b in a if b.strip()]
        a.reverse()
        a.pop(0)
        columsFormated.append(a)

for Move in movements:
    moveNums = [int(i) for i in Move.split() if i.isdigit()]
    numToMove = moveNums[0]
    numMoveFrom = moveNums[1]
    numMoveTo = moveNums[2]
    # Part 2
    if (numToMove > 1):
        moveMultiColums = columsFormated[numMoveFrom - 1][-numToMove:]
        columsFormated[numMoveFrom - 1] = columsFormated[numMoveFrom - 1][:-numToMove]
        columsFormated[numMoveTo - 1] += moveMultiColums 
    else:
        columsFormated[int(numMoveTo) - 1].append(columsFormated[int(numMoveFrom) - 1].pop())

# Results
print("".join([x[-1] for x in columsFormated]))