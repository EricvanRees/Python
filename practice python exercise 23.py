
# coding: utf-8

# In[ ]:


'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
'''

# open first file and create empty list to store all integers from file
f = open("primenumbers.txt", "r") 
a = []

# use a for loop to iterate over the file contents, convert strings to integers
# and add them to list
for line in f:
    a.append(int(line))

# create an empty list and repeat the same procedure for file 2
b = []
# create an empty list to store the integers that are in file 1 and 2
c = []
g = open("happynumbers.txt", "r")
for line in g:
    b.append(int(line))
   
    # run a for loop to append integers in a and b to c
    for i in a:
        if i in a and i in b:
            c.append(i)
        else:
            continue

# convert list with overlapping integers to a set
myset = set(c)
new_list = list(myset)
# print the set with overlapping integers
print(new_list)

