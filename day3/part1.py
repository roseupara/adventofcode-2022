import string
input = open("day3/input.txt")

#Part 1
inputValues = input.read().split("\n")

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

ruckSack = 0

for items in inputValues: 
    if(items != ""): 
        firstContainer = slice(0, len(items)//2)
        secondContainer = slice(len(items)//2, len(items))
        for letter in list(items[firstContainer]): 
            if(letter in items[secondContainer]): 
                if(letter not in lowercase): 
                    ruckSack += uppercase.index(letter) + 27
                    break
                else: 
                    ruckSack += lowercase.index(letter) + 1
                    break

#Results
print(ruckSack)
