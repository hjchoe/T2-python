# James Choe
# add_four.py
# 12/17/2020

from colorama import Fore, Back, Style
import random

A = int(input(Fore.YELLOW + "\nWhat is the first number? " + Fore.WHITE))
print(f"The first number is {A}.")

B = int(input(Fore.YELLOW + "\nWhat is the second number? " + Fore.WHITE))
print(f"The second number is {B}.")

X = A + B
print(Fore.CYAN + f"The Total of A and B is {X}.")

C = int(input(Fore.YELLOW + "\nWhat is the third number? " + Fore.WHITE))
print(f"The third number is {C}.")

Y = X + C
print(Fore.CYAN + f"The Total of A, B, and C is now {Y}.")

D = int(input(Fore.YELLOW + "\nWhat is the fourth number? " + Fore.WHITE))
print(f"The fourth number is {D}.")

Z = Y + D
print(Fore.CYAN + f"The Total is now {Z}.")

print(Style.RESET_ALL)