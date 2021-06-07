# James Choe
# Assignment 4.1.4- Dice Roll Numbers
# 2/8/2021

import random
from colorama import Fore, Back, Style

sides = [1, 2, 3, 4, 5, 6]

numoftimes = int(input(Fore.BLUE + "How many times would you like to roll the dice?\n" + Fore.WHITE))

for x in range(1, numoftimes+1):
    diceone = sides[random.randint(0, 5)]
    dicetwo = sides[random.randint(0, 5)]
    dicesum = diceone + dicetwo
    print(Fore.GREEN + f"\nRoll {x}:\n" + Fore.YELLOW + f"Dice 1: {diceone}\n" + f"Dice 2: {dicetwo}\n" + f"Sum: {dicesum}")

print(Style.RESET_ALL)