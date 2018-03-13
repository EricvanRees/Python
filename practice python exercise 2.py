
# coding: utf-8

# In[ ]:


# this program asks the user for a number. if the number is even, the user will be prompted a message confirming this.
# if the number is uneven, the user will receive a message confirming this.

user_input = input("Please enter a positive integer: ")
if int(user_input) % 2 == 0:
    print("The number is even")
else:
    print(" The number is even")

