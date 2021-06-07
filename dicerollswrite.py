# James Choe
# Assignment 4.1.4- Dice Roll Numbers
# 3/4/2021

import random
from colorama import Fore, Back, Style
import os

if os.path.exists("dicerolls.txt"):
    src = os.path.realpath("dicerolls.txt")
    f = open(src, "w+")
else:
    f = open("dicerolls.txt", "w+")

sides = [1, 2, 3, 4, 5, 6]

numoftimes = int(input(Fore.BLUE + "How many times would you like to roll the dice?\n" + Fore.WHITE))

for x in range(1, numoftimes+1):
    diceone = sides[random.randint(0, 5)]
    dicetwo = sides[random.randint(0, 5)]
    dicesum = diceone + dicetwo
    diceinfo = [diceone, dicetwo, dicesum]
    f.write(f"{diceinfo}\n")

print(Style.RESET_ALL)
f.close()