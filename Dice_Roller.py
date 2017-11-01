#This program will prompt for the number of sides, dice, and rolls
#and output the results, then ask if the user would like to start over

import sys
import math
from random import randint

def rollDice():
    global numberSides, numberDice, numberRolls
    rollCount = 1
    while numberRolls > 0:
        print("Roll "+ str(rollCount) + ":", end=" ")
        diceCount = numberDice
        while diceCount > 0:
            print(randint(1, numberSides), end=" ")
            print
            diceCount-=1
        print()
        numberRolls -= 1
        rollCount += 1

while True:
    print("Welcome!")
    numberSides = int(input("How many sides should the dice have? "))
    print("----The dice will have "+str(numberSides)+" sides")
    numberDice = int(input("How many dice would you like to roll? "))
    print("----There will be "+str(numberDice)+" dice")
    numberRolls = int(input("How many times would like to roll the dice? "))
    print("----There will be "+str(numberRolls)+" rolls")

    rollDice()
    print()
    print("Done.")
    print()
    while True:
        answer = input("Would you like to start over? (y/n): ")
        if answer in ("y", "n"):
            break
        print("Invalid input.")
    if answer == "y":
        continue
    else:
        print("Goodbye")
        break
