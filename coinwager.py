# James Choe
# Assignment 4.1.7- Coin Wager
# 2/11/2021

import random
from colorama import Fore, Back, Style

bank = 10.0

def coinflip():
    choices = ["heads", "tails"]
    result = choices[random.randint(0, 1)]
    return result

def checkbal(bank):
    if bank <= 0.0:
        playstatus = False
    else:
        playstatus = True
    return playstatus

def checkwager(wager, bank):
    if wager > bank:
        wagerstatus = False
    else:
        wagerstatus = True
    return wagerstatus

def bet(bank):
    while True:
        betamt = input(Fore.BLUE + "\nHow much would you like to bet?\n" + Fore.WHITE)
        try:
            betamt = float(betamt)
            if betamt == 0.0:
                print(Fore.RED + "You can't bet nothing.")
                continue
            elif betamt > bank:
                print(Fore.RED + "You can't bet more than you have. Balance: " + Fore.YELLOW + '$' + str(bank))
                continue
            elif betamt <= bank:
                break
            else:
                print(Fore.RED + "Invalid input.")
        except:
            print(Fore.RED + "Invalid input.")
    return betamt

def makechoice():
    while True:
        choice = input(Fore.BLUE + "\nHeads or Tails? " + Fore.CYAN + "(1 - Heads | 2 - Tails)\n" + Fore.WHITE)
        if choice == "1":
            choice = "heads"
            break
        elif choice == "2":
            choice = "tails"
            break
        else:
            print(Fore.RED + "Improper input.")
    return choice

def checkwin(choice, result):
    if choice == result:
        win = True
        print(Fore.GREEN + "\nWIN")
    else:
        win = False
        print(Fore.RED + "\nLOSE")
    return win

def transaction(win, betamt, bank):
    if win == True:
        bank += betamt
    else:
        bank -= betamt
    return bank

def menu(bank):
    print(Fore.YELLOW + f"\nBalance: ${bank}")
    while True:
        playstatus = checkbal(bank)
        if playstatus == True:
            play = input(Fore.BLUE + "Would you like to bet on a coin flip? " + Fore.CYAN + "(1 - yes | 2 - no)\n" + Fore.WHITE)
            if play == "1":
                betamt = bet(bank)
                choice = makechoice()
                print(Fore.BLUE + "\nYou: " + Fore.WHITE + choice)
                result = coinflip()
                print(Fore.BLUE + "Coin: " + Fore.MAGENTA + result)
                win = checkwin(choice, result)
                bank = transaction(win, betamt, bank)
                print(Fore.BLUE + "\nNew Balance: " + Fore.YELLOW + '$' + str(bank))
                continue
            elif play == "2":
                profit = bank - 10.0
                print("\n" + Fore.MAGENTA + "RESULTS:\n" + Fore.BLUE + "You have a balance of: " + Fore.YELLOW + '$' + str(bank) + Fore.BLUE + "\nYou made: " + Fore.YELLOW + '$' + str(profit))
                break
            else:
                print(Fore.RED + "Improper Input\n")
        elif playstatus == False:
            print(Fore.RED + "\nYou do not have enough funds to play again.")
            break

menu(bank)

print(Style.RESET_ALL)