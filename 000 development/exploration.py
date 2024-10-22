# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 10:03:46 2019

@author: taras
"""

##url="https://histolines.wordpress.com/"

###https://stackoverflow.com/questions/35809554/how-to-download-google-image-search-results-in-python

keyword='iphone11'
path="C:/Users/taras/Desktop/histolines/data/general image/data/"+keyword


import pandas as pd


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


import time
from collections import Counter
import datetime
from skimage import io       
from icrawler.builtin import GoogleImageCrawler

import glob
files = glob.glob('*.jpg')



google_crawler = GoogleImageCrawler(storage={'root_dir': path})
google_crawler.crawl(keyword=keyword, max_num=100)


name="000001"
img = io.imread(path+'/'+name+'')

print(i)
plt.imshow(img)



# Create a function that will parse the html from the given URL.  It'll then scrape the fields including:
# Name, reviews, rating, etc.  

###https://www.geeksforgeeks.org/how-to-download-google-images-using-python/



def read_data(url):
    url="https://www.google.com/search?q=cat&rlz=1C1CHBF_enUS795US795&sxsrf=ACYBGNSskJi2oVCo14qf1clgvsrcoJeV_g:1574005957106&source=lnms&tbm=isch&sa=X&ved=0ahUKEwje-8mPzfHlAhURRK0KHUNwDy4Q_AUIEigB&biw=1536&bih=775"
    print(url)
    my_page = urlopen(url)
    my_soup = soup(my_page, "html.parser")
    ##print (my_soup)
    data = []
    names=[]
    times=[]
    imgs=[]  # Create an empty list to store the data
    i=0
    containers = my_soup.findAll("div", {"class":"post-content clear-fix"})  # Searches for the specific html class to store scraped data
    for container in containers:  
        #data.append(container)
        #print (container)
    
        img = container.find("img") # name of the restaurants
        try:
                img=img.get('src')
        except AttributeError:
                print (img)
        #print (img)
        imgs.append(img)
        
    containers = my_soup.findAll("header", {"class":"post-title"})  # Searches for the specific html class to store scraped data
    for container in containers:  
        data.append(container)
        ##print (container)
        #print (i)
        i=i+1
        ##print (container)
        name = container.find("h1").text.strip() # name of the restaurants
        names.append(name)
        #print (name)
    containers = my_soup.findAll("p", {"class":"post-date"})  # Searches for the specific html class to store scraped data
    for container in containers:  
        data.append(container)
        ##print (container)
        #print (i)
        i=i+1
        ##print (container)
        month = container.find("span").text.strip() # name of the restaurants
        date= container.find("strong").text.strip() # name of the restaurants
        times.append(date+" "+month)
        ##print (month)
        #print (date)
    ##time published
        
    dataframe=pd.DataFrame()
    dataframe['text'] = names
    dataframe['imgs'] = imgs
    dataframe['times'] = times
    return dataframe
