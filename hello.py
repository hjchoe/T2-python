# James Choe
# Hello Introduction
# 12/14/2020

from colorama import Fore, Back, Style

print(Fore.GREEN + "\nHello Dave")

name = "Dave"

print(Fore.WHITE + "\nHello " + name)

name = input(Fore.YELLOW + "\nEnter your name: " + Fore.WHITE)
print(Fore.WHITE + "Hello " + name)

age = input(Fore.YELLOW + "\nEnter your age: " + Fore.WHITE)
hometown = input(Fore.YELLOW + "Enter your hometown: " + Fore.WHITE)
grade = input(Fore.YELLOW + "Enter your grade: " + Fore.WHITE)
favorite_food = input(Fore.YELLOW + "Enter your favorite food: " + Fore.WHITE)

print(Fore.WHITE + f"""\nHi my name is {name}! I live in {hometown} and I'm in grade {grade}. My favorite food is {favorite_food}.""")

print(Style.RESET_ALL)