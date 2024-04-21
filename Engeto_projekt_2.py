"""
projekt_1.py: druhý projekt do Engeto Online Python Akademie
author: Martin Vopalecky
email: mvopale@email.cz
discord: martin_21315
"""

import random

def uvodni_vypis():
    print("-----------------------------------------------")
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    return()

def vytvor_tajne_cislo():
    return ''.join(random.sample('123456789', 1) + random.sample('0123456789', 3))

def vyhodnot_tip(tajne_cislo, tip):
    bulls = sum(a==b for a, b in zip(tajne_cislo, tip))
    cows = len(set(tajne_cislo) & set(tip)) - bulls
    return bulls, cows

def hra():
    uvodni_vypis()
    
    tajne_cislo = vytvor_tajne_cislo()
    pocet_pokusu = 0
    
    while True:
        tip = input("Enter a number: ")
        if len(tip) != 4 or not tip.isdigit() or len(set(tip)) != 4 or tip[0] == '0':
            print("Invalid input, please try again.")
            continue
        
        pocet_pokusu += 1
        bulls, cows = vyhodnot_tip(tajne_cislo, tip)
        if bulls == 4:
            print("-----------------------------------------------")
            print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses!")
            print("-----------------------------------------------")
            break
        else:
            print(f"{bulls} bull{'s' if bulls > 1 else ''}, {cows} cow{'s' if cows > 1 else ''}")

if __name__ == "__main__":
    hra()
