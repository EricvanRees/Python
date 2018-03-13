#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     13/03/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class myString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s= raw_input()

    def printString(self):
        print self.s.upper()

strObj = myString()
strObj.getString()
strObj.printString()
