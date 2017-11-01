#This program will ask for a number and then check if it's even or odd

import sys
import math

numberTest = int(input("Pick a number: "))

if numberTest % 2 == 0:
    print(numberTest, " is an even number!")
else:
    print(numberTest, " is an odd number!")
