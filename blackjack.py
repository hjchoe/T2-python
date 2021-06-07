# James Choe
# Assignment 4.2.1- Blackjack
# 2/15/2021

import random
from colorama import Fore, Back, Style

suites = ['S', 'C', 'H', 'D']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
bank = 100

def makedeck(suites, numbers):
    deck = []
    for suite in suites:
        for number in numbers:
            deck.append(number + suite)
    return deck

def shuffle(deck):
    ndeck = deck[:]
    random.shuffle(ndeck)
    return ndeck

def hitdeck(deck, hand):
    card = random.choice(deck)
    deck.pop(deck.index(card))
    hand.append(card)
    return hand, deck

def dealerhit(deck, hand):
    value = calcdeck(hand)
    while value < 17:
        card = random.choice(deck)
        deck.pop(deck.index(card))
        hand.append(card)
        value = calcdeck(hand)
    return hand

def calcdeck(hand):
    value = 0
    face = ['T', 'J', 'Q', 'K']
    aces = []
    for card in hand:
        num = card[0:1]
        if num in face:
            value += 10
        elif num == 'A':
            aces.append('A')
        else:
            num = int(num)
            value += num
    for ace in aces:
        if value + 11 > 21:
            value += 1
        else:
            value += 11
    return value

def checkblackjack(hand):
    value = calcdeck(hand)
    if value > 21:
        result = False
    elif value == 21:
        result = True
    else:
        result = value
    return result

def playerdeal(deck, hand):
    card1 = random.choice(deck)
    deck.pop(deck.index(card1))
    card2 = random.choice(deck)
    deck.pop(deck.index(card2))
    hand.append(card1)
    hand.append(card2)
    return deck, hand

def dealerdeal(deck, dealerhand):
    card = random.choice(deck)
    deck.pop(deck.index(card))
    dealerhand.append(card)
    return deck, dealerhand

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

def checkbal(bank):
    if bank <= 0.0:
        playstatus = False
    else:
        playstatus = True
    return playstatus

def transaction(win, betamt, bank):
    if win == True:
        bank += betamt
    else:
        bank -= betamt
    return bank

def setupround(basedeck):
    hand = []
    dealerhand = []
    playdeck = shuffle(basedeck)
    playdeck, dealerhand = dealerdeal(playdeck, dealerhand)
    playdeck, hand = playerdeal(playdeck, hand)
    return playdeck, dealerhand, hand

def won(bank, bet):
    bank += bet
    print(Fore.GREEN + "\nWON")
    print(Fore.MAGENTA + "\nNew Balance: " + Fore.YELLOW + str(bank))
    return bank

def lost(bank, bet):
    bank -= bet
    print(Fore.RED + "\nLOST")
    print(Fore.MAGENTA + "\nNew Balance: " + Fore.YELLOW + str(bank))
    return bank

def tie(bank):
    print(Fore.BLUE + "\nTIE")
    print(Fore.MAGENTA + "\nBalance: " + Fore.YELLOW + str(bank))

def displayall(hand, dealerhand, betamt):
    showdealer = ""
    showhand = ""
    for card in dealerhand:
        showdealer += f"{card} "
    for card in hand:
        showhand += f"{card} "
    print(Fore.CYAN + "\nDealer:\n" + Fore.MAGENTA + showdealer)
    print(Fore.CYAN + "\nPlayer:\n" + Fore.MAGENTA + showhand)
    print(Fore.BLUE + "\nBet Amount: " + Fore.YELLOW + str(betamt))

# setup
basedeck = makedeck(suites, numbers)

while True:
    playstatus = checkbal(bank)
    if playstatus == True:
        playstate = input(Fore.BLUE + "\nWould you like to play? (1 - Yes | 2 - No)\n" + Fore.WHITE)
        if playstate == '1':
            betamt = bet(bank)
            playdeck, dealerhand, hand = setupround(basedeck)
            dresult = checkblackjack(dealerhand)
            hresult = checkblackjack(hand)
            if dresult == True and hresult == False:
                displayall(hand, dealerhand, betamt)
                bank = lost(bank, betamt)
            elif dresult == False and hresult == True:
                displayall(hand, dealerhand, betamt)
                bank = won(bank, betamt)
            elif dresult == True and hresult == True:
                displayall(hand, dealerhand, betamt)
                tie(bank)
            else:
                while True:
                        displayall(hand, dealerhand, betamt)
                        choice = input(Fore.BLUE + "\nHit or Stand? (1 - hit | 2 - stand)\n" + Fore.WHITE)
                        if choice == '1':
                            hand, deck = hitdeck(playdeck, hand)
                            hresult = checkblackjack(hand)
                            if hresult == True:
                                displayall(hand, dealerhand, betamt)
                                bank = won(bank, betamt)
                                break
                            elif hresult == False:
                                displayall(hand, dealerhand, betamt)
                                bank = lost(bank, betamt)
                                break
                            else:
                                pass
                        elif choice == '2':
                            dealerhand = dealerhit(playdeck, dealerhand)
                            dresult = checkblackjack(dealerhand)
                            if dresult == True:
                                displayall(hand, dealerhand, betamt)
                                bank = lost(bank, betamt)
                                break
                            elif dresult == False:
                                displayall(hand, dealerhand, betamt)
                                bank = won(bank, betamt)
                                break
                            else:
                                if hresult > dresult:
                                    displayall(hand, dealerhand, betamt)
                                    bank = won(bank, betamt)
                                    break
                                elif hresult < dresult:
                                    displayall(hand, dealerhand, betamt)
                                    bank = lost(bank, betamt)
                                    break
                                else:
                                    displayall(hand, dealerhand, betamt)
                                    tie(bank)
                                    pass
                            break
                        else:
                            print(Fore.RED + "Invalid Input")
        elif playstate == '2':
            print(Fore.MAGENTA + f"\nFinal Balance: " + Fore.YELLOW + f"${bank}")
            break
        else:
            print(Fore.RED + "Improper Input" + Fore.WHITE)
    else:
        print(Fore.RED + "\nYou do not have enough funds to play again.")
        break



print(Style.RESET_ALL)