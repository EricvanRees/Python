
# coding: utf-8

# In[ ]:


'''
In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary 
from a JSON file on disk, rather than having the dictionary defined in the program.

script uses a file called birthdays.json which contents are:

{
    "Hans Kazan": "1/7/1965",
    "Hans Klok": "1/8/1972",
    "Eric van Rees": "5/2/1980",
    "Ivo Niehe":  "6/5/1957",
    "Karel Appel": "2/3/1933"
}
'''

import json

with open("birthdays.json", "r") as f:
    info = json.load(f)
    
    name = input("Please enter a name for checking the person´s birthday: ")

    if name in info:
        print("The corresponding birthday is: " + str(birthday_dic[name]))
    else:
        print("No valid name given")

