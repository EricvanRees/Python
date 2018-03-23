
# coding: utf-8

# In[ ]:


'''Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.'''

import random

def main():
    answer = input("Would you like to generate a new password? Y/N: ")
    if answer == "Y":
        i = []
        b = 0
        while b < 11:
            a = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            i.append(a)
            b +=1
        print("Your new password is: " + "".join(i))
    
if __name__ == '__main__':
    main()

