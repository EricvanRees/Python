#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     11/03/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Find the sum of all the multiples of 3 or 5 below 1000.

a = []

for x in range(1,1000):
   if x % 3 == 0:
    a.append(x)
    continue
   elif x % 5 == 0:
    a.append(x)
    continue
   else:
        continue

print sum(a)



