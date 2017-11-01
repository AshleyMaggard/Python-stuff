#This program chooses a number and then prompts the user to guess it
#Optional todo: gui, options to tell warm/cold or high/low, error handling
import sys
from random import randint


#while True:
    #Program start here#######
print("Ok, I'm thinking of a positive integer greather than 0 but less than 10,000.")
number = randint(1, 9999)
#print("testing: the number is", number)
while True:
    guess = int(input("Take a guess and I'll tell you if you're close:  "))
    if guess == number:
        print("Congratulations! You guessed my number! It was",number,".")
        print("Goodbye")
        break
    elif number-10 <= guess <= number+10:
        print("Call the fire department because you're on fire!")
    elif number-100 <= guess <= number+100:
        print("You're burning up!")
    elif number-1000 <= guess <= number+1000:
        print("You're really warm!")
    elif number-2000 <= guess <= number+2000:
        print("You're warm!")
    elif number-3000 <= guess <= number+3000:
        print("You're cold!")
    elif number-4000 <= guess <= number+4000:
        print("You're really cold!")
    elif number-9999 <= guess <= number+9999:
        print("You're freezing!")
    else:
        print("Invalid input. Try again.")
        continue
