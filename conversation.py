# James Choe
# conversation.py
# 12/14/2020

from colorama import Fore, Back, Style
import random

name = input(Fore.YELLOW + "\nHey whats your name?\n" + Fore.WHITE)
print(Fore.YELLOW + f"\nNice to meet you {name}.")

age = input(Fore.YELLOW + "\nHow old are you?\n" + Fore.WHITE)
print(Fore.YELLOW + f"\nNo way! I'm {age} too!")

hometown = input(Fore.YELLOW + "\nWhat town do you live in?\n" + Fore.WHITE)
if hometown == "South Hamilton":
    print(Fore.YELLOW + f"Wow I live in {hometown} as well!")
else:
    print(Fore.YELLOW + f"{hometown}, that sounds like a nice town. I live in South Hamilton!")

grade = input(Fore.YELLOW + "\nWhat about your grade?\n" + Fore.WHITE)
computerGrade = random.randint(9, 12)
if str(computerGrade) == grade:
    print(Fore.YELLOW + f"That's cool, I'm in grade {computerGrade} too!")
else:
    print(Fore.YELLOW + f"Grade {grade}? Nice, I'm in grade {computerGrade}.")

favorite_food = input(Fore.YELLOW + "\nWhat's your favorite food?\n" + Fore.WHITE)
print(Fore.YELLOW + f"Mmmm, {favorite_food}... that sounds really good.")

print(Fore.YELLOW + f"\nWell, it was nice meeting you {name}, bye!")

print(Style.RESET_ALL)