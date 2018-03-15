
# coding: utf-8

# In[ ]:


'''Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)'''

a = input("please enter a string: ")

if a == a[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")

