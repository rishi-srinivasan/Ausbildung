# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:32:37 2022

@author: Rishi Srinivasan
"""

from bs4 import BeautifulSoup, SoupStrainer
import requests
import os
import pandas as pd
#from urllib.request import Request, urlopen
#import re
import httplib2

#Initializing variables
im = []
alt = []
url = 'https://medium.com/coders-camp/all-machine-learning-algorithms-models-explained-adcd95d5fb3c'
df = pd.DataFrame(columns={'Title':'','Link':''})               #Create the dataframe with the links and title

#Method to get all images url in webpage and save it in a csv file
def getimage(url,folder):    
    try:
        res = os.path.isdir(os.path.join(os.getcwd(),folder))   #Checks if there already exists a directory in the name - 'image_links'
        if res == False:
            os.mkdir(os.path.join(os.getcwd(),folder))          #If not then create a directory in the name 'image_links'
            os.chdir(os.path.join(os.getcwd(),folder))          #Change the working directory to the created directory
        r = requests.get(url)
        #r = Request(url)
        #html = urlopen(r.full_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        #images = soup.find_all('au mw')
        for link in soup.find_all('a'):
            alt.append(link.get('href'))
            #im.append(img['src'])
        df['Title'] = pd.Series(alt)
        #df['Link'] = pd.Series(im)
        df.to_csv('100_ML_with_python.csv',sep=';')
        print("Downloaded all the image links!")
    except:
        print('There is an exception!')
        pass
    
#Call the getimage()
getimage(url,'image_links')

#folder = 'image_links'