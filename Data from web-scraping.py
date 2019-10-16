#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as BS

#url = input('Enter the url: ')
html = urllib.request.urlopen('https://stackoverflow.com/questions/48481290/a-simple-way-to-view-ipython-notebook').read()
soup = BS(html, 'html.parser')

print(soup)
#get all anchor tags
tags = soup('p')
for tag in tags:
    print(tag.get('href', None))


# In[ ]:




