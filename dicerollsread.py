# James Choe
# Assignment 4.1.4- Dice Roll Numbers
# 3/4/2021

import random
from colorama import Fore, Back, Style
import re
import os

if os.path.exists("dicerolls.txt"):
    src = os.path.realpath("dicerolls.txt")
else:
    print('file not found')
    exit()

f = open(src, "r")

rfile = f.readlines()

results = []
for result in rfile:
    result = re.findall("\d+", result)
    intresult = []
    for num in result:
        intresult.append(int(num))
    results.append(intresult)

def numofdoubles(list):
    num = 0
    for i in list:
        if i[0] == i[1]:
            num += 1
    return num

def maxminsum(list):
    maxN = 0
    minN = 13
    for i in list:
        if i[3] > maxN:
            maxN = i[3]
        if i[3] < minN:
            minN = i[3]
    return maxN, minN

def numofsums(list, search):
    num = 0
    for i in list:
        if i[3] == int(search):
            num += 1
    return num


doubles = numofdoubles(results)
maxnum, minnum = maxminsum(results)
print(Fore.MAGENTA + "Data:\n" + Fore.YELLOW + "Number of doubles: " + Fore.WHITE + str(doubles) + Fore.YELLOW + "\nGreatest Sum: " + Fore.WHITE + str(maxnum) + Fore.YELLOW + "\nSmallest Sum: " + Fore.WHITE + str(minnum))

while True:
    ans = input(Fore.BLUE + "\nWould you like to find how many times a certain sum is in the results? (yes | no):\n" + Fore.WHITE)
    if ans == "yes":
        while True:
            search = input(Fore.BLUE + "\nEnter sum you would like to search for:\n" + Fore.WHITE)
            if search.isdigit():
                numofsearch = numofsums(results, search)
                print(Fore.GREEN + f"{search} is a sum {numofsearch} times")
                break
            else:
                print(Fore.RED + "Invald Input")
    elif ans == "no":
        exit()
    else:
        print(Fore.RED + "Invalid Input")

print(Style.RESET_ALL)
f.close()