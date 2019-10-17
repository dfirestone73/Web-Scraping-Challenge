#!/usr/bin/env python
# coding: utf-8

# In[123]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo





# In[124]:


def init_browser():
    return Browser()

def scrape():

# In[125]:

    browser=Browser()


# In[ ]:


#NASA Mars News


# In[13]:
    complete_dict = {}

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')


# In[16]:


    news_title=soup.find('div',class_='content_title')
    news_title=news_title.text.strip()
    complete_dict['news_titles'] = news_title

# In[18]:


    paragraph_text=soup.find('div',class_='article_teaser_body')
    complete_dict['paragraph_texts']=paragraph_text

# In[ ]:


# JPL Mars Space Images - Featured Image


# In[134]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')


# In[135]:


    featured_image=soup.find(class_='button fancybox')


# In[138]:


    featured_image=featured_image['data-fancybox-href']


# In[139]:


    featured_image_url='https://www.jpl.nasa.gov'+featured_image
    complete_dict['feature_image']=featured_image_url


# In[ ]:


# Mars Weather


# In[74]:


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')


# In[78]:


    mars_weather=soup.find(class_='tweet-text')
    mars_weather=mars_weather.text.strip()
    complete_dict['mars_weathers']=mars_weather


# In[8]:


# Mars Facts


# In[83]:


    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')


# In[84]:


    MarsFacts=pd.read_html('https://space-facts.com/mars/')[1]



# In[85]:


    MarsFacts=MarsFacts.rename(columns={0:'Planet Profile',1:'Values'})



# In[94]:


    MarsFacts=MarsFacts.to_html(buf=None, columns=None, col_space=None, header=True, index=True)
    complete_dict['marsfacts']=MarsFacts

# In[22]:


# Mars Hemispheres


# In[93]:


#main_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[143]:


    url='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    cerberus=soup.find(class_='wide-image')
    cerberus_img='https://astrogeology.usgs.gov'+cerberus['src']



# In[144]:


    url='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    schiaparelli=soup.find(class_='wide-image')
    schiaparelli_img='https://astrogeology.usgs.gov'+schiaparelli['src']



# In[146]:


    url='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    syrtis_major=soup.find(class_='wide-image')
    syrtis_major_img='https://astrogeology.usgs.gov'+syrtis_major['src']



# In[147]:


    url='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    valles_marineris=soup.find(class_='wide-image')
    valles_marineris_img='https://astrogeology.usgs.gov'+valles_marineris['src']



# In[148]:


    hemisphere_image_urls=[{'title':'Cerberus Hemisphere','img_url':'cerberus_img'},
                      {'title':'Schiaparelli Hemisphere','img_url':'schiaparelli_img'},
                      {'title':'Syrtis Major Hemisphere','img_url':'syrtis_major_img'},
                      {'title':'Valles Marineris Hemisphere','img_url':'valles_marineris_img'}]


# In[149]:


    complex['hemisphere_images']=hemisphere_image_urls


# In[ ]:


    return complete_dict

