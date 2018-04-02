
# coding: utf-8

# In[ ]:


'''Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and
another number. The function decides whether or not the given number is 
inside the list and returns (then prints) an appropriate boolean.'''


def my_f():
    x = [int(x) for x in input("please enter a list of ordered numbers, separated by a comma: ").split()]
    my_number = int(input("please input a number to check if it´s in the list: "))

    if my_number in x:
        print("True") 
    else:
        print("False")

my_f()

