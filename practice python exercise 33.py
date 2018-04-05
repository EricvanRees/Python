
# coding: utf-8

# In[ ]:


'''For this exercise, we will keep track of when our friend’s birthdays are.
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. '''

birthday_dic = {
    "Hans Kazan": "1/7/1965",
    "Hans Klok": "1/8/1972",
    "Eric van Rees": "5/2/1980",
    "Ivo Niehe":  "6/5/1957",
    "Karel Appel": "2/3/1933"
}

name = input("Please enter a name for checking the person´s birthday: ")

if name in birthday_dic:
    print("The corresponding birthday is: " + str(birthday_dic[name]))
else:
    print("No valid name given")

