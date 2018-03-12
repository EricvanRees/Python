#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     12/03/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()
'''

#solution 1, using lists instead of dict:

my_dict = {}
lista = []
listb = []
x = input("enter a whole number: ")

for x in range(1,x):
    keys = lista.append(x)
    values = listb.append(int(x*x))
    print zip(lista, listb)

#solution 2:
n=int(raw_input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print d
