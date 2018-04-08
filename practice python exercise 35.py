
# coding: utf-8

# In[ ]:


'''
In the previous exercise we saved information about famous scientists’ names and birthdays to disk.
In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
and count how many scientists have a birthday in each month.
'''

import json
from collections import Counter

#define json contents
birthdays = {
    "Albert Einstein": "14/03/1879",
    "Stephen Hawking": "08/01/1942",
    "Isaac Newton": "04/01/1643",
    "Galileo Galilei": "15/02/1564"
}

#write json file to disk
with open("info.json", "w") as f:
    json.dump(birthdays, f)

# open json file and read dictionary items
with open("info.json", "r") as f:
    info = json.load(f)
    # put dictionary values in a list to be able to slice only month references
    c = list(info.values())
    # create empty list for all month references
    month_list = []
    # define for loop to append all month references to list
    for i in c:
        month_list.append(i[3:5])
        # count all instances of separate months with Counter() function
        c = Counter(month_list)
    # print how many scientists have their birthday in a given month using values of c
    print("There are {} scientists with a birthday in January, {} in February and {} in March".format(c["01"], c["02"], c["03"]))

