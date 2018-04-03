
# coding: utf-8

# In[ ]:


'''Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file, 
and print out the results to the screen.'''

'''this code counts all instances of substring "Lea" in the text file'''

with open('nameslist.txt', 'r') as open_file:
    # read all text in file into a variable that contains text as a string
    all_text = open_file.read()
    # define substring to count instances of substring
    sub1 = "Lea"
    sub2 = "Luke"
    sub3 = "Darth"
    b = ["Lea", "Luke", "Darth"]
    # print a count of all instances of substring in text = 54
    print("There are " + str(all_text.count(sub1)) + " instances of Lea")
    print("There are " + str(all_text.count(sub2)) + " instances of Luke")
    print("There are " + str(all_text.count(sub3)) + " instances of Darth")

