#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     22/03/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ?)'''

def fib():
    a = int(raw_input("Enter how many fibonacci numbers to calculate: "))
    fibonacci_numbers = [0, 1]
    for i in range(2,a):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

    return fibonacci_numbers

print(fib())
