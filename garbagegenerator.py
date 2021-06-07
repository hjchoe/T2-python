# James Choe
# Assignment 4.3.1- Garbage Generator
# 2/25/2021

import random

#f = open("/Users/hjcho/Dropbox/programming/T2 python/garbage.txt", 'w+')
f = open("/Users/School_Account/Dropbox/programming/T2 python/garbage.txt", 'w+')

while True:
    numofgar = input("\nEnter how many garbage characters you want:\n")
    if isinstance(int(numofgar), int):
        numofgar = int(numofgar)
        break
    else:
        print("Improper Input")
        pass

garbchrs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
garbstr = []
for x in range(numofgar):
    randomchar = random.choice(garbchrs)
    garbstr.append(randomchar)

code = input("\nWhat is your code?\n")
codechrs = []
for char in code:
    codechrs.append(char)

numofgar
numofcod = len(code)
aproxspace = round(numofgar/(numofcod+1))

i = aproxspace
for char in codechrs:
    garbstr[i] = char
    i += aproxspace

finalgarb = ''
for char in garbstr:
    finalgarb += char

f.write(finalgarb)
f.close()

print('\nmade garbage in: garbage.txt\n')

#f = open("/Users/hjcho/Dropbox/programming/T2 python/garbage.txt", 'r')
f = open("/Users/School_Account/Dropbox/programming/T2 python/garbage.txt", 'r')

code = f.readlines()

characters = []
for line in code:
    for char in line:
        characters.append(char)

chrl = len(garbchrs)
for i in range(chrl):
    maxchar = ''
    maxn = 1000000
    diffchars = []
    for char in characters:
        if char not in diffchars:
            curn = characters.count(char)
            if curn == 1:
                chrl += 1
            if curn < maxn:
                maxn = curn
                maxchar = char
            diffchars.append(char)

    for x in range(maxn):
        characters.pop(characters.index(maxchar))

    print(maxn, maxchar)

f.close()