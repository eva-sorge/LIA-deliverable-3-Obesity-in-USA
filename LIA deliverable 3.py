#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 21:14:13 2025

@author: evasorge
"""

#1. Introduction:
    
#The dataset we are using compares age, gender, height, weight, BMI, activity level and obesity level. The question to which we would like to visualize the answer is wether or not higher physical inactivity levels correlates to increased obesity across the US. To this question, we would also like to answer if there is a correlation between gender and higher BMI. 

#2. Preliminary steps:
    
import pandas as pd
data = pd.read_csv('obesity_data.csv')

#a): 
data.head(10)
data.tail(10)
#These functions show the first and last ten entries of our data
print(data.shape)
#The data shape is 1000 entries through 7 columns
data.info()
#This function provides insight on the category names, the amount of non-null values for each category, the types of variables and the amount of variables
data.describe()
#This function shows the amount of variables for each category, and provides the mean, standard dev., minimum, maximum and 25%, 50% and 75% quartiles
data.size
#This shows the amount of values we have in our data (we can see that there are values for everything)
data.dtypes
#This function orovides insight on the types of values for each category

#b):
data.duplicated()
data.drop_duplicates()  #this is the data we can use to plot graphs, to make them more visually pleasing and less confusing

#c):
print(data.isnull())
