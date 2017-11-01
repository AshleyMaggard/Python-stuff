# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
import sys
import math

# def multipleOfThree():
#     k = 1
#     while k <= 333:
#         print(3*k)
#         k += 1
#
# def multipleOfFive():
#     m = 1
#     while m <= 199:
#         print(5*m)
#         m += 1

# multipleOfThree()
# multipleOfFive()

multiplesOfThree = range(0,1000,3)
multiplesOfFive = range(0,1000,5)

listOfThree = []
for i in multiplesOfThree:
    listOfThree.append(i)

listOfFive = []
for j in multiplesOfFive:
    listOfFive.append(j)

sumAll = sum(listOfFive+listOfThree)


print()
print("Multiples of 3 below 1000:")
print(listOfThree)
print()
print()
print("Multiples of 5 below 1000:")
print(listOfFive)
print()
print()
print("The sum of all multiples of 3 and 5 below 1000 is: ",sumAll)
