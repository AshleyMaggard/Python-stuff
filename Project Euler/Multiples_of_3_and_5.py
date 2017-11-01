# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys
import math
import time

start_time = time.clock()

multiplesOfThree = range(0,1000,3)
multiplesOfFive = range(0,1000,5)
multiplesOfBoth = range(0,1000,15)

listOfThree = []
for i in multiplesOfThree:
    listOfThree.append(i)

listOfFive = []
for j in multiplesOfFive:
    listOfFive.append(j)

mergedList = list(set(listOfThree + listOfFive))

sumAll = sum(list(mergedList))

print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("=                                                                                   =")
print("= This is problem #1 from Project Euler. It will list all the multiples of 3 & 5    =")
print("= below 100 (and remove duplicates). It will then output the sum of that list.      =")
print("=                                                                                   =")
print("=                                                            Code by Ashley Maggard =")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print()
print("---Multiples of 3 & 5 below 1000:---")
print(mergedList)
print()
print()
print()
print(">>The sum of all multiples of 3 and 5 below 1000 is: ",sumAll)
print()
print(">>>>>Calculation took", round(time.clock() - start_time,5), "seconds")
