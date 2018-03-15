
# coding: utf-8

# In[ ]:


'''Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.'''

# my_list = [x for x in my_list if x.attribute == value]

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = [x for x in a if x % 2 == 0]
print(a)

