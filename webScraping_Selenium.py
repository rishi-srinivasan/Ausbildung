# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:03:14 2022

@author: Rishi Srinivasan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

url1 = 'https://www.ausbildung.de/unternehmen/globus-fachmaerkte-gmbh-co-kg/stellen/ausbildung-auszubildender-m-w-d-zum-verkaeufer-ab-august-2022-globus-baumarkt-berlin-lichtenberg-dhehgetm/51c64dcd-2d42-4549-8597-02d59eda1544/'
url2 = ''

#Initialize chrome driver
driver = webdriver.Chrome('D:\Academics\HTW Berlin\Winter Semester 2021-22\M15 Project Studies on Contemporary Topics\Chrome Driver\chromedriver.exe')

#Open website
driver.get(url1)

#Maximize window
driver.maximize_window()

df_fact = pd.DataFrame(columns={'title':'','value':''})

lab = []
val = []

#XPath locator - XPath for finding short facts in ausbildung.de 
xpath1 = '//li[@class="facts-list__fact"]/div/span[1]'
xpath2 = '//li[@class="facts-list__fact"]/div/span[2]'

lab1 = driver.find_elements(by=By.XPATH, value=xpath1)
lab2 = driver.find_elements(by=By.XPATH, value=xpath2)

for i,j in zip(lab1,lab2):
    lab.append(i.get_attribute('textContent'))
    val.append(j.get_attribute('textContent'))

#Class locator - class name for finding short facts in ausbildung.de
lab1 = driver.find_elements(by=By.CLASS_NAME, value='label')
lab2 = driver.find_elements(by=By.CLASS_NAME, value='value')

for i,j in zip(lab1,lab2):
    lab.append(i.get_attribute('textContent'))
    val.append(j.get_attribute('textContent'))

#ID locator - class name for finding short facts in ausbildung.de
lab1 = driver.find_elements(by=By.ID, value='ID')
lab2 = driver.find_elements(by=By.ID, value='ID')

for i,j in zip(lab1,lab2):
    lab.append(i.get_attribute('textContent'))
    val.append(j.get_attribute('textContent'))





for label,value in zip(driver.find_element_by_xpath(xpath1),driver.find_element_by_xpath(xpath2)):
    lab.append(label)
    val.append(value)
    
