import random
from os import path

if path.exists("statescapitals.txt"):
    src = path.realpath("statescapitals.txt")

# open file this time to only read, type: "r"
f = open(src, "r")

# var = f.readlines() reads the txt file and puts each lined into a list: var
lines = f.readlines()

# finding how many states+capitals are in the txt file by iterating and adding to the count var
leng = 0
for line in lines:
    if line != None: # make sure the line isn't nothing
        leng += 1

while True:
    # asking whether the player would like to answer with the state or the capital
    gametype = input("\nWould you like to guess the state or the capital? (1 - state | 2 - capital):\n")

    # making sure the input answered is either 1 or 2 not something else
    if gametype == '1' or gametype == '2':
        break
    else:
        print("invalid input")

# setting points to 0
points = 0
while True:
    # choose a random integer from 1 - leng (number of entries in the txt file earlier) to choose a random state+capital
    x = random.randint(1, leng)

    # since we put each of the state+capitals into a list, we look at that list and find the state+capital using the index: x
    sANDc = lines[x]

    # the index of the ':' to find where the separator between state and capital is
    index = sANDc.find(':')

    # the state would be characters 0 (inclusive) to index of ':' (exclusive)
    state = sANDc[0:index]

    # the capital would be characters index of ':' + 1 (inclusive) to the final character len(sANDc) - 1 (exclusive)
    capital = sANDc[index+1:len(sANDc)-1]

    # guessing state vs guessing capital from earlier
    if gametype == '1':
        # question
        answer = input(f"\nWhat state is {capital} the capital of?\n")
        
        # checking whether answer is correct
        if answer == state:
            print("\nGood Job")
            
            # add a point
            points += 1
        else:
            print(f"\nWrong\nRight answer: {state}")
            # if the answer is wrong, break is used to leave the while loop = GAME OVER
            break

    # guessing state vs guessing capital from earlier
    elif gametype == '2':
        # question
        answer = input(f"\nWhat is the capital of {state}?\n")
        
        # checking whether answer is correct
        if answer == capital:
            print("\nGood Job")
            
            # add a point
            points += 1
        else:
            print(f"\nWrong\nRight answer: {capital}")
            # if the answer is wrong, break is used to leave the while loop = GAME OVER
            break

# when game is over, prints final score
print(f"\nFinal Score: {points}\n")

f.close()