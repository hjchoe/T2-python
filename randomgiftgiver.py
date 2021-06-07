# James Choe
# Assignment 4.1.8- Random Gift Giver
# 2/11/2021

import random
from colorama import Fore, Back, Style

def exchangegifts(plist):
    giftlist = plist[:]
    usedx = []
    for person in plist:
        if person != None:
            while True:
                x = random.randint(0, len(plist)-1)
                if x == plist.index(person):
                    continue
                elif x in usedx:
                    continue
                else:
                    giftlist[x] = person
                    plist[plist.index(person)] = None
                    usedx.append(x)
                    break
    print(Fore.MAGENTA + "\nGift List:" + Fore.YELLOW)
    for gift in giftlist:
        print(f"{gift}'s gift")
    return giftlist

def results(perlist, giflist):
    print(Fore.GREEN + "\nResults:" + Fore.YELLOW)
    for thing in perlist:
        print(f"{thing} gets {giflist[perlist.index(thing)]}'s gift")

def validname(name, nlist):
    for n in nlist:
        if n == name:
            return False
        else:
            pass
    return True

def createlist():
    personentered = ''
    people = []
    print(Fore.BLUE + "\nEnter a person's name you'd like to add, type 'done' when you are finished:\n" + Fore.WHITE)
    while True:
        personentered = input()
        if personentered == "done":
            if len(people) > 1:
                break
            else:
                print(Fore.RED + "There needs to be more than 1 person in the gift exchange." + Fore.WHITE)
        else:
            state = validname(personentered, people)
            if state == True:
                people.append(personentered)
                continue
            elif state == False:
                print(Fore.RED + "Name is already in the list." + Fore.WHITE)
    print(Fore.MAGENTA + "\nPeople in gift exchange:" + Fore.YELLOW)
    for person in people:
        print(person)
    return people

peoplelist = createlist()
newpeoplelist = peoplelist[:]
giftlist = exchangegifts(newpeoplelist)
results(peoplelist, giftlist)

print(Style.RESET_ALL)