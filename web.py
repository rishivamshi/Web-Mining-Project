# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:13:12 2017

@author: rishi
"""

import timeit
start = timeit.default_timer()

'''
from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame

url = 'https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/HYD_MAA_24-09-2017?contains=false&remove='

result = requests.get(url)
c = result.content


soup = BeautifulSoup(c)
summary = soup.find("div",{'class':'price_sectn'})
tables = summary.find_all("p",class_= 'ng-binding')
print(tables)
'''




a = input()
b = input()

url = "https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/"+a+"_"+b+"_24-09-2017?contains=false&remove="


from selenium import webdriver
chrome_path = r"C:\Python27\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


driver.get(url)
'''
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "listing_row")))'''

price = driver.find_elements_by_class_name("airline_info_detls")

for post in price:
    print(post.text)

'''timeCa
html_page =  driver.page_source
driver.quit

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_page)
summary = soup.find("div",{'class':'listing_row'})
tables = summary.find_all("div",class_= 'listing_row')
print(tables)
'''
















        


stop = timeit.default_timer()
print (stop - start )