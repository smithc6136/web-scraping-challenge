#!/usr/bin/env python
# coding: utf-8

# In[2]:


#CURRENT PROBLEMS:
#Mars hemispheres website - link not printing (last step for each hemisphere)


# In[3]:


# Dependencies
from bs4 import BeautifulSoup
import requests


# In[4]:


# NASA Mars News: URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[5]:


# Import Splinter and set the chromedriver path
from splinter import Browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[6]:


# Retrieve page
browser.visit(url)


# In[7]:


#using splinter
browser.is_element_present_by_css("div.article_teaser_body", wait_time=10)


# In[8]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(browser.html, 'html.parser')


# In[9]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[10]:


title = soup.find_all("div", class_= "content_title")[1].get_text()
title
#Sample code: img_url = soup.find("img", class_="jpg")["src"]


# In[11]:


news_paragraph = soup.find("div", class_="article_teaser_body").get_text()
news_paragraph


# In[12]:


#JPL Mars Space Images: url of page to be scraped 
images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[13]:


# Import Splinter and set the chromedriver path
from splinter import Browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[14]:


# Retrieve page
browser.visit(images_url)


# In[15]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(browser.html, 'html.parser')


# In[16]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[17]:


link=soup.find(id= 'full_image')
link


# In[18]:


#use splinter to click through website to get to desired image
click_image = browser.find_by_id('full_image')
click_image.click()


# In[19]:


browser.is_element_present_by_text("more info", wait_time=5)
more_info = browser.links.find_by_partial_text("more info")
more_info.click()


# In[20]:


#Recreate soup
soup = BeautifulSoup(browser.html, 'html.parser')


# In[21]:


result_link = soup.find(class_= 'main_image').get('src')
result_link


# In[22]:


featured_image_url = "https://www.jpl.nasa.org" + result_link
featured_image_url


# In[23]:


import pandas as pd


# In[24]:


#Mars facts: URL of page to be scraped
facts_url="https://space-facts.com/mars/"


# In[25]:


tables = pd.read_html(facts_url)
tables


# In[26]:


# We can slice off any of those dataframes that we want using normal indexing.
df = tables[0]
df.columns = ['variable', 'measurement']
df.head()


# In[27]:


#Set the index to the State column
df.set_index('variable', inplace=True)
df.head()


# In[28]:


# Pandas to_html method generates HTML tables from DataFrames.
html_table = df.to_html()
html_table


# In[29]:


#Mars Hemispheres: URL of page to be scraped
hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[30]:


# Import Splinter and set the chromedriver path
from splinter import Browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[31]:


# Retrieve page
browser.visit(hemisphere_url)


# In[32]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(browser.html, 'html.parser')


# In[33]:


#CERBERUS HEMISPHERE: use splinter to click through website to get to desired image
cerberus_hemisphere = browser.links.find_by_partial_text("Cerberus Hemisphere Enhanced")
cerberus_hemisphere.click()


# In[34]:


#use splinter to click through website to get to desired image
cerberus_hemisphere_image = browser.links.find_by_partial_text("Sample")
cerberus_hemisphere_image.click()


# In[35]:


#Recreate soup
soup = BeautifulSoup(browser.html, 'html.parser')


# In[36]:


cerberus_link = soup.find('img').get('src')
cerberus_link


# In[37]:


cerberus_full_link = "https://www.jpl.nasa.gov" + cerberus_link
cerberus_full_link


# In[38]:


# Retrieve page
browser.visit(hemisphere_url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(browser.html, 'html.parser')


# In[39]:


#SCHIAPARELLI HEMISPHERE: use splinter to click through website to get to desired image
Schiaparelli_hemisphere = browser.links.find_by_partial_text("Schiaparelli Hemisphere Enhanced")
Schiaparelli_hemisphere.click()


# In[40]:


#use splinter to click through website to get to desired image
Schiaparelli_hemisphere_image = browser.links.find_by_partial_text("Sample")
Schiaparelli_hemisphere_image.click()


# In[41]:


#Recreate soup
soup = BeautifulSoup(browser.html, 'html.parser')


# In[42]:


Schiaparelli_link = soup.find('img').get('src')
Schiaparelli_link


# In[43]:


Schiaparelli_full_link = "https://www.jpl.nasa.gov" + Schiaparelli_link
Schiaparelli_full_link


# In[44]:


# Retrieve page
browser.visit(hemisphere_url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(browser.html, 'html.parser')


# In[45]:


#SYRTIS MAJOR HEMISPHERE: use splinter to click through website to get to desired image
Syrtis_Major_hemisphere = browser.links.find_by_partial_text("Syrtis Major Hemisphere Enhanced")
Syrtis_Major_hemisphere.click()


# In[46]:


#use splinter to click through website to get to desired image
Syrtis_Major_hemisphere_image = browser.links.find_by_partial_text("Sample")
Syrtis_Major_hemisphere_image.click()


# In[47]:


#Recreate soup
soup = BeautifulSoup(browser.html, 'html.parser')


# In[48]:


Syrtis_Major_link = soup.find('img').get('src')
Syrtis_Major_link


# In[49]:


Syrtis_Major_full_link = "https://www.jpl.nasa.gov" + Syrtis_Major_link
Syrtis_Major_full_link


# In[50]:


# Retrieve page
browser.visit(hemisphere_url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(browser.html, 'html.parser')


# In[51]:


#VALLES MARINERIS HEMISPHERE: use splinter to click through website to get to desired image
Valles_Marineris_hemisphere = browser.links.find_by_partial_text("Valles Marineris Hemisphere Enhanced")
Valles_Marineris_hemisphere.click()


# In[52]:


#use splinter to click through website to get to desired image
Valles_Marineris_hemisphere_image = browser.links.find_by_partial_text("Sample")
Valles_Marineris_hemisphere_image.click()


# In[53]:


#Recreate soup
soup = BeautifulSoup(browser.html, 'html.parser')


# In[54]:


Valles_Marineris_link = soup.find('img').get('src')
Valles_Marineris_link


# In[55]:


Valles_Marineris_full_link = "https://www.jpl.nasa.gov" + Valles_Marineris_link
Valles_Marineris_full_link


# In[67]:


# Append the dictionary with the image url string and hemisphere title to a list with one dictionary per hemisphere.
hemisphere_image_urls = [
    { 'Title': 'Valles Marineris Hemisphere', "img_url": Valles_Marineris_full_link},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_full_link},
    {"title": "Schiaparelli Hemisphere", "img_url": Schiaparelli_full_link},
    {"title": "Syrtis Major Hemisphere", "img_url": Syrtis_Major_full_link},
]
hemisphere_image_urls


# In[56]:


# Iterate through all pages
for x in range(50):
   # HTML object
   html = browser.html
   # Parse HTML with Beautiful Soup
   soup = BeautifulSoup(html, 'html.parser')
   # Retrieve all elements that contain book information
   articles = soup.find_all('div', class_='itemLink product-item')

#     # Iterate through each book
#     for article in articles:
#         # Use Beautiful Soup's find() method to navigate and retrieve attributes
#         h3 = article.find('h3')
#         link = h3.find('a')
#         href = link['href']
#         title = link['title']
#         print('-----------')
#         print(title)
#         print('http://books.toscrape.com/' + href)


# In[57]:


# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("scrape_mars.py")


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




