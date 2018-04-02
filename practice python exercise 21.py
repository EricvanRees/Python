
# coding: utf-8

# In[3]:


'''Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, 
use the code from the solution), and instead of printing the results to a screen, 
write the results to a txt file. In your code, just make up a name for the file you are saving to.'''

# import the requests Python library for programmatically making HTTP requests
import requests
# import the BeautifulSoup Python library
from bs4 import BeautifulSoup

# the URL of the NY Times website we want to parse
base_url = 'http://www.nytimes.com'

# the syntax (according to the documentation) for how to 
# "load" a webpage through Python
r = requests.get(base_url)

# how to decode the text of the HTML of the NY Times homepage
# website. r comes from the requests request above
soup = BeautifulSoup(r.text, 'lxml')
 
# find and loop through all elements on the page with the 
# class name "story-heading"
with open('file_to_save.txt', 'w') as open_file:
    for story_heading in soup.find_all(class_="story-heading"): 
    # for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely
        if story_heading.a: 
            open_file.write(story_heading.a.text.replace("\n", " ").strip())
            open_file.write("\n")
        else: 
            open_file.write(story_heading.contents[0].strip())
            open_file.write("\n")

