
# coding: utf-8

# In[ ]:


'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. '''

a = [5, 10, 15, 20, 25]
b = []
for i in a:
    b.append(a[0])
    b.append(a[-1])
    break
    
print(b)

