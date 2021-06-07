# James Choe
# Assignment 4.1.4- Dice Roll Numbers
# 2/8/2021

import random
from colorama import Fore, Back, Style

sides = int(input(Fore.BLUE + "How many sides per dice?\n" + Fore.WHITE))
numofdice = int(input(Fore.BLUE + "How many dice per roll?\n" + Fore.WHITE))
numofrolls = int(input(Fore.BLUE + "How many times would you like to roll the dice?\n" + Fore.WHITE))

for x in range(1, numofrolls+1):
    print(Fore.GREEN + f"\nRoll {x}:")
    dicesum = 0
    for y in range(1, numofdice+1):
        dicenum = random.randint(1, sides)
        print(Fore.YELLOW + f"Dice {y}: {dicenum}")
        dicesum += dicenum
    print(f"Sum: {dicesum}")
    
print(Style.RESET_ALL)