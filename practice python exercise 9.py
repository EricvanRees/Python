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

import random
a = random.randint(1, 9)
b = raw_input("This is a guessing game. Type a number between 1 and 9: ")
guess = 0

while True and guess < 5:
    guess += 1
    if int(b) < a:
        b = raw_input("Too low! Try again: ")
    elif int(b) > a:
        b = raw_input("Too high! Try again: ")
    else:
        print("Correct! You win! It took you " + str(guess) + " guess(es).")
        break

