import random
import os
import time

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    healthStat = ((rollDice(6) * rollDice(12)) / 2) + 10
    return healthStat

def strength():
    strengthStat = ((rollDice(6) * rollDice(8)) / 2) + 12
    return strengthStat

while True:
    print("⚔️ Battle Time ⚔️")
    print()
    c1Name = input("Enter your hero's name: ")
    c1Race = input("Enter your race: ")
    print()
    print(c1Name)
    c1Health = health()
    c1Strength = strength()
    print("Health:", c1Health)
    print("Strength:", c1Strength)
    print()
    print("Name your nemesis")
    print()

    c2Name = input("Enter your nemesis' name: ")
    c2Race = input("Enter race: ")
    print()
    print(c2Name)
    c2Health = health()
    c2Strength = strength()
    print("Health:", c2Health)
    print("Strength:", c2Strength)
    print()

    round = 1
    winner = None

    while True:
        time.sleep(1)
        os.system('clear')
        print("⚔️ Battle Time ⚔️")
        print()
        print("The Battle is on!\n")

        c1Dice = rollDice(6)
        c2Dice = rollDice(6)

        difference = abs(c1Strength - c2Strength) + 1

        if c1Dice > c2Dice:
            c2Health -= difference
            if round == 1:
                print(c1Name + " strikes first!\n")
            else:
                print(c1Name + " wins round", round,"\n")
        elif c2Dice > c1Dice:
            c1Health -= difference
            if round == 1:
                print(c2Name + " strikes first!\n")
            else:
                print(c2Name + " wins round", round,"\n")
        else:
            print("Swords clash and sparks fly as round", round, "ends in a draw!\n")

        print(c1Name)
        print("Health:", c1Health)
        print()
        print(c2Name)
        print("Health:", c2Health)
        print()

        if c1Health <= 0:
            print(c1Name, "has died!\n")
            winner = c2Name
            break
        elif c2Health <= 0:
            print(c2Name, "has died!\n")
            winner = c1Name
            break
        else:
            round += 1
            print("Round", round, "is about to begin!")
            time.sleep(2)
            os.system('clear')
            print("⚔️ Battle Time ⚔️")
            print()

    print(winner, "is victorious in", round, "rounds! 🏆")
    break