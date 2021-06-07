# James Choe
# Assignment 4.1.2- Coin Flip
# 2/8/2021

import random
from colorama import Fore, Back, Style

answers = ["Heads", "Tails"]
results = [""]

def listprint(list):
    for result in list:
        print(Fore.GREEN + result)

while True:
    question = input(Fore.BLUE + "\nFlip a coin? (Y - yes | N - no)\n" + Fore.WHITE)

    if question == "Y":
        side = answers[random.randint(0, 1)]
        print(Fore.GREEN + side)
        results.append(side)
        continue
    elif question == "N":
        print(Fore.BLUE + "\nList of Results:")
        listprint(results)
        break
    else:
        print("Improper input.")

print(Style.RESET_ALL)