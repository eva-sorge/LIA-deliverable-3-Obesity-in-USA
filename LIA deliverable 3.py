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
print(data.shape)
data.info()
data.describe()
data.size
data.dtypes

#b):
data.duplicated()
data.drop_duplicates()  #this is the data we can use to plot graphs, to make them more visually pleasing and less confusing

#c):
