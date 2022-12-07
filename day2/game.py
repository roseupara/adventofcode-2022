input = open("day2/puzzle.txt")

inputValues = input.read().split("\n")

def getPoints(input): 
    if(input == "X"): 
        return 1
    elif(input == "Y"):
        return 2
    elif(input == "Z"): 
        return 3
    else: 
        return 0

def toWin(input):
    if(input == "A"):
        return "Y"
    elif(input == "B"):
        return "Z"
    elif(input == "C"):
        return "X"
    
def isTie(input): 
    if(input == "A"):
        return "X"
    elif(input == "B"): 
        return "Y"
    elif(input == "C"):
        return "Z"

# Part 2
def toLose(input):
    if(input == "C"):
        return "Y"
    elif(input == "B"):
        return "X"
    elif(input == "A"):
        return "Z"

totalScore = 0; 

for game in inputValues:
    valuesFormatted = game.split(" ")

    opponent = valuesFormatted[0]
    response = valuesFormatted[1]

# Part 2
    if (response == "Y"):
        response = isTie(opponent)
    elif (response == "X"):
        response = toLose(opponent)
    elif (response == "Z"):
        response = toWin(opponent)


    if(isTie(opponent) == response):
        # Draw
        totalScore += getPoints(response) + 3
    else:
        if(toWin(opponent) == response):
            # Win
            totalScore += getPoints(response) + 6
        else:
            # Loss
            totalScore += getPoints(response)

#Result
print(totalScore)

