#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     21/03/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#(_Hint: remember to use the user input lessons from the very first exercise

#Extras:
#Keep the game going until the user types ?exit?
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
a = random.randint(1, 9)
b = raw_input("This is a guessing game. Type a number between 1 and 9 or exit to stop: ")
guess = 0

while True:
    guess += 1
    if b == "exit":
        print "exit game"
        break

    if int(b) < a:
        b = raw_input("Too low! Try again or exit: ")
    elif int(b) > a:
        b = raw_input("Too high! Try again or exit: ")
    else:
        print("Correct! You win! It took you " + str(guess) + " guess(es).")
        break

