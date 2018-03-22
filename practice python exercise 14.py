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

'''Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.'''

def define_list():
    my_list = raw_input("please enter a list of numbers separated by a comma: ").split(",")
    a = list(my_list)
    return a

def set_list(a):
    my_set = set(a)
    my_list = list(my_set)
    print my_list

set_list(define_list())