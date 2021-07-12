# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:35:52 2021

@author: Eben Emmanuel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def avg_date_2013():
    temp_i= 0
    average= []
    for rows in pd.read_csv('Data/AQI/aqi2013.csv', chunksize= 24):
        add_var= 0
        avg= 0.0
        data= []
        df= pd.DataFrame(data= rows)    ## Converting the initial 24 rows as DataFrames.
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp= float(i)
                    add_var += temp
        
        avg= add_var/24
        temp_i += 1
        
        average.append(avg)
    return average
        
    
def avg_date_2014():
    temp_i= 0
    average= []
    for rows in pd.read_csv('Data/AQI/aqi2014.csv', chunksize= 24):
        add_var= 0
        avg= 0.0
        data= []
        df= pd.DataFrame(data= rows)    ## Converting the initial 24 rows as DataFrames.
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp= float(i)
                    add_var += temp
        
        avg= add_var/24
        temp_i += 1
        
        average.append(avg)
    return average
        
    
def avg_date_2015():
    temp_i= 0
    average= []
    for rows in pd.read_csv('Data/AQI/aqi2015.csv', chunksize= 24):
        add_var= 0
        avg= 0.0
        data= []
        df= pd.DataFrame(data= rows)    ## Converting the initial 24 rows as DataFrames.
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp= float(i)
                    add_var += temp
        
        avg= add_var/24
        temp_i += 1
        
        average.append(avg)
    return average
        
    
def avg_date_2016():
    temp_i= 0
    average= []
    for rows in pd.read_csv('Data/AQI/aqi2016.csv', chunksize= 24):
        add_var= 0
        avg= 0.0
        data= []
        df= pd.DataFrame(data= rows)    ## Converting the initial 24 rows as DataFrames.
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp= float(i)
                    add_var += temp
        
        avg= add_var/24
        temp_i += 1
        
        average.append(avg)
    return average
     
        
def avg_date_2017():
    temp_i= 0
    average= []
    for rows in pd.read_csv('Data/AQI/aqi2017.csv', chunksize= 24):
        add_var= 0
        avg= 0.0
        data= []
        df= pd.DataFrame(data= rows)    ## Converting the initial 24 rows as DataFrames.
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp= float(i)
                    add_var += temp
        
        avg= add_var/24
        temp_i += 1
        
        average.append(avg)
    return average
     

def avg_date_2018():
    temp_i= 0
    average= []
    for rows in pd.read_csv('Data/AQI/aqi2018.csv', chunksize= 24):
        add_var= 0
        avg= 0.0
        data= []
        df= pd.DataFrame(data= rows)    ## Converting the initial 24 rows as DataFrames.
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp= float(i)
                    add_var += temp
        
        avg= add_var/24
        temp_i += 1
        
        average.append(avg)
    return average
        
        
if __name__ == '__main__':
    lst2013= avg_date_2013()
    lst2014= avg_date_2014()
    lst2015= avg_date_2015()
    lst2016= avg_date_2016()
    lst2017= avg_date_2017()
    lst2018= avg_date_2018()

    #Plotting
    plt.plot(range(0,365),lst2013, label= '2013 data')
    plt.plot(range(0,364),lst2014, label= '2014 data')
    plt.plot(range(0,365),lst2015, label= '2015 data')
    plt.plot(range(0,365),lst2016, label= '2016 data')
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc= 'upper right')
    plt.show()