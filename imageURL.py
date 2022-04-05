# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 09:37:51 2022

@author: Rishi Srinivasan
"""

from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

#Initializing variables
im = []
alt = []
url = 'https://www.ausbildung.de/berufe/anaesthesietechnischer-assistent/'
df = pd.DataFrame(columns={'Title':'','Link':''})

#Method to get all images url in webpage and save it in a csv file
def getimage(url,folder):    
    try:
        res = os.path.isdir(os.path.join(os.getcwd(),folder))   #Checks if there already exists a directory in the name - 'image_links'
        if res == False:
            os.mkdir(os.path.join(os.getcwd(),folder))          #If not then create a directory in the name 'image_links'
            os.chdir(os.path.join(os.getcwd(),folder))          #Change the working directory to the created directory
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            alt.append(img['alt'])
            im.append(img['src'])
        df['Title'] = pd.Series(alt)
        df['Link'] = pd.Series(im)
        df.to_csv('img_url.csv',sep=';')
        print("Downloaded all the image links!")
    except:
        print('There is an exception!')
        pass
    
#Call the getimage()
getimage(url,'image_links')
   
#Create the dataframe with the links and title

