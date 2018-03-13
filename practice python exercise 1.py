
# coding: utf-8

# In[ ]:


# A small program that asks users for their age and tells them when they turn 100

my_input = input("Please enter your name")
my_input2 = str(input("Hello " + my_input + " please enter your age ")) 
new_year = 2118 - int(my_input2)
print("You will turn 100 in the year " + str(new_year))

