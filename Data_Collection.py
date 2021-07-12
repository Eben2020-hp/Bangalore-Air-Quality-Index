# -*- coding: utf-8 -*-
"""
Created on Mon July 12 8:30:45 2021

@author: Eben Emmanuel
"""

import os
import time
import requests      ## Helps us to download the required page in the form of html.
import sys


## To retrieve Data
def retrive_html():
    for year in range(2013, 2019):
        for month in range (1,13):
            if (month < 10):
                url= 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month, year)
            else:
                url= 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month, year)
        
        
            texts= requests.get(url)     ## To retrieve the url.
            text_utf= texts.text.encode('utf=8')    ## We need to do UTF encoding due to some characters in the html that we need to fix.
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):   ## Will check if our folder is there.. If not then we will create it.
                os.makedirs("Data/Html_Data/{}".format(year))
            
            with open("Data/Html_Data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_utf)
            
            sys.stdout.flush()

     
if __name__ == '__main__':
    start_time = time.time()
    retrive_html()
    stop_time = time.time()
    print('Time Taken: ',stop_time-start_time)
    


