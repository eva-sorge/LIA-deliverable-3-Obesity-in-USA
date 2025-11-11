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
#These functions show the first and last ten entries of our data.
print(data.shape)
#The data shape is 1000 entries through 7 columns.
data.info()
#This function provides insight on the category names, the amount of non-null values for each category, the types of variables and the amount of variables.
data.describe()
#This function shows the amount of variables for each category, and provides the mean, standard dev., minimum, maximum and 25%, 50% and 75% quartiles.
data.size
#This shows the amount of values we have in our data (we can see that there are values for everything).
data.dtypes
#This function provides insight on the types of values for each category.

#b):
data.duplicated()
data.drop_duplicates()  #this is the data we can use to plot graphs, to make them more visually pleasing and less confusing.

#c):
print(data.isnull())
#As seen in part a) through the info and size functions, there are no null values in any of the categories from our dataset. This is reinforced by the isnull() function.

#d):
#Using the info function, we can see that BMI is stored as a datetime type instead of numerical values. We can convert this using the pd.to_numeric() function
data["BMI"] = pd.to_numeric(data["BMI"])
data.info()  #this shows that our conversion was successful

#3. Univariate non-graphical EDA:
#The numerical values for this dataset are Age, Height, Weight, BMI and Physical Activity Level
#Age:
print("Mean:", data["Age"].mean())
print("Median:", data["Age"].median())
print("Mode:", data["Age"].mode())
print("Standard dev.:", data["Age"].std())
print("Variance:", data["Age"].var())
print("Skewness:", data["Age"].skew())
print("Kurtosis:", data["Age"].kurt())
print("Quartiles:", data["Age"].quantile([0.25, 0.50, 0.75]))

#Once we have this principle down, we can use a loop to do the next numerical columns:

#Height, Weight, BMI, Phyical Activity Level:
for values in ["Height", "Weight", "BMI", "PhysicalActivityLevel"]:
    print(values)
    print("Mean:", data[values].mean())
    print("Median:", data[values].median())
    print("Mode:", data[values].mode())
    print("Standard dev.:", data[values].std())
    print("Variance:", data[values].var())
    print("Skewness:", data[values].skew())
    print("Kurtosis:", data[values].kurt())
    print("Quartiles:", data[values].quantile([0.25, 0.50, 0.75]))

#The categorical variables for this dataset are Gender and Obesity Category:
for values in ["Gender", "ObesityCategory"]:
    print("Frequency counts:", data[values].value_counts())
    print("Proportions:", data[values].value_counts()/1000)
    print("Mode:", data[values].mode())
#This shows us that the majority of people surveyed for this dataset are within a Normal Weight range, and that most people were Male.
    
    



    