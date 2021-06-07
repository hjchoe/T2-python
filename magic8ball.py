# James Choe
# Assignment 4.1.1- Magic 8 Ball
# 2/8/2021

import random
from colorama import Fore, Back, Style

answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so."]

question = input(Fore.BLUE + "What would you like to ask the magic 8 ball?\n" + Fore.WHITE)

print(Fore.BLUE + answers[random.randint(0, 7)])

print(Style.RESET_ALL)