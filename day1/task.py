N = [c.strip() for c in open('day1/numbers.txt')]

L = []
for elf in ('\n'.join(N)).split('\n\n'):
    c = 0
    for x in elf.split('\n'):
        c += int(x)
    L.append(c)
L = sorted(L)

#First Part
print(L[-1])
#Second Part
print(L[-1]+L[-2]+L[-3])