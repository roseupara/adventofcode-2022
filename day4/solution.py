input = open("day4/input.txt")
inputValues = input.read().split("\n")

#Part 1 & 2
sum = 0

for pair in inputValues: 
    firstPair = pair.split(",")[0].split("-")
    secondPair = pair.split(",")[1].split("-")
    for section in range(int(firstPair[0]) + 1, int(firstPair[1])):
        firstPair.append(str(section))
    for section in range(int(secondPair[0]) + 1, int(secondPair[1])):
        secondPair.append(str(section))

    firstPair = [int(x) for x in firstPair]
    secondPair = [int(x) for x in secondPair]
    firstPair.sort()
    secondPair.sort()

    # Part 2
    firstPair = list(dict.fromkeys(firstPair))
    secondPair = list(dict.fromkeys(secondPair))
    combied = firstPair + secondPair
    
    if set(firstPair).issuperset(set(secondPair)):
        sum += 1
    elif set(secondPair).issuperset(set(firstPair)):
        sum += 1
    # Part 2
    elif len(combied) != len(set(combied)):
        sum += 1

#Result
print(sum)