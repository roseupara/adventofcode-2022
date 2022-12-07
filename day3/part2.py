import string
input = open("day3/input.txt")

#Part 2

inputValues = input.read().split("\n")

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

ruckSack = 0
line = 0 
itemsList = []

for items in inputValues: 
    if(items != "" and line == 2): 
        line = 0
        itemsList.append(items)
        for letter in itemsList[0]: 
            if(letter in itemsList[1] and letter in itemsList[2]): 
                if(letter not in lowercase): 
                    ruckSack += uppercase.index(letter) + 27
                    break
                else:
                    ruckSack += lowercase.index(letter) + 1
                    break
        itemsList = []
    else:
        itemsList.append(items)
        line += 1

#Result
print(ruckSack)
