
# coding: utf-8

# In[ ]:


'''Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.'''

def get_prime():
    number = int(input("Give me a number to check if it´s a prime number: "))
    if number == 1:
        print("number is not a prime number")
    elif number == 2:
        print("number is a prime number")
    elif number % 2 == 0:
        print("number is not a prime number")
    else:
        if number % 2 != 0:
            if number % number == 0:
                print("number is a prime number")
            else:
                print("number is not a prime number")

get_prime()

