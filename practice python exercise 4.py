
# coding: utf-8

# In[15]:


'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

a = int(input("Please enter a number to divide: "))
my_list = []
for i in range(1, a+1):
    if a % i == 0:
        my_list.append(i)
    

print(my_list)

