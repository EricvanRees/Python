
# coding: utf-8

# In[ ]:


'''Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.'''

a = input("Write a sentence - the word order will be reversed next: ")
a = a.split()
print(" ".join(a[::-1]))

