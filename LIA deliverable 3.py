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
    
#4 Univariate graphical EDA

import seaborn as sns
import matplotlib.pyplot as plt

#BMI

#a) Custom and appropriate number of bins 
sns.displot(data, x="BMI" , bins=20 )
#b) Conditioning on other variables
sns.displot(data, x="BMI", hue="Gender", bins=20)
plt.title("BMI VS GENDER")
#c) Stacked histogram
sns.displot(data, x="BMI", hue="ObesityCategory" , bins=20 , multiple="stack")
#d) Dodge bars
sns.displot(data, x="BMI", hue="ObesityCategory",bins=10, multiple="dodge")
#e) Normalized histogram statistics
sns.displot(data, x="BMI", hue="ObesityCategory", stat="density" ,common_norm=False)
#f) Kernel density estimation (choosing the smoothing bandwidth)
sns.displot(data, x="BMI", kind="kde" , bw_adjust=2)
#g) Empirical cumulative distributions
sns.displot(data, x="BMI", hue="ObesityCategory", kind="ecdf")

#WEIGHT

#a) Custom and appropriate number of bins
sns.displot(data, x="Weight" , bins=20 )
#b) Conditioning on other variables
sns.displot(data, x="Weight", hue="Gender", bins=20)
#c) Stacked histogram
sns.displot(data, x="Weight", hue="ObesityCategory" , bins=20 , multiple="stack")
#d) Dodge bars
sns.displot(data, x="Weight", hue="ObesityCategory",bins=10, multiple="dodge")
#e) Normalized histogram statistics
sns.displot(data, x="Weight", hue="ObesityCategory", stat="density" ,common_norm=False)
#f) Kernel density estimation (choosing the smoothing bandwidth)
sns.displot(data, x="Weight", kind="kde" , bw_adjust=2)
#g) Empirical cumulative distributions
sns.displot(data, x="Weight", hue="ObesityCategory", kind="ecdf")

#HEIGHT

#a) Custom and appropriate number of bins
sns.displot(data, x="Height" , bins=20 )
#b) Conditioning on other variables
sns.displot(data, x="Height", hue="Gender", bins=20)
#c) Stacked histogram
sns.displot(data, x="Height", hue="ObesityCategory" , bins=20 , multiple="stack")
#d) Dodge bars
sns.displot(data, x="Height", hue="ObesityCategory",bins=10, multiple="dodge")
#e) Normalized histogram statistics
sns.displot(data, x="Height", hue="ObesityCategory", stat="density" ,common_norm=False)
#f) Kernel density estimation (choosing the smoothing bandwidth)
sns.displot(data, x="Height", kind="kde" , bw_adjust=2)
#g) Empirical cumulative distributions
sns.displot(data, x="Height", hue="ObesityCategory", kind="ecdf")

#non-continuous variables (AGE AND PHYSICAL ACTIVITY )

#PHYSICAL ACTIVITY

#a) Custom and appropriate number of bins
sns.displot(data, x="PhysicalActivityLevel" , bins=10 )
#b) Conditioning on other variables
sns.displot(data, x="PhysicalActivityLevel", hue="Gender", bins=10)
#c) Stacked histogram
sns.displot(data, x="PhysicalActivityLevel", hue="ObesityCategory" , bins=10 , multiple="stack")
#d) Dodge bars
sns.displot(data, x="PhysicalActivityLevel", hue="ObesityCategory",bins=10, multiple="dodge")

#this variable is not continuous enough to have normalized histogram , ecdf and kde

# AGE

#a) Custom and appropriate number of bins
sns.displot(data, x="Age" , bins=10 )
#b) Conditioning on other variables
sns.displot(data, x="Age", hue="Gender", bins=10)
#c) Stacked histogram
sns.displot(data, x="Age", hue="ObesityCategory" , bins=10 , multiple="stack")
#d) Dodge bars
sns.displot(data, x="Age", hue="ObesityCategory",bins=10, multiple="dodge")

#this variable is not continuous enough to have normalized histogram , ecdf and kde


#5 Multivariate non-graphical EDA

import pandas as pd 

# a (different variables ) and b (normalize)

print(pd.crosstab(data["ObesityCategory"], data["Gender"]))
print(pd.crosstab(data["ObesityCategory"], data["Gender"], normalize=True))
print(pd.crosstab(data["Gender"], data["PhysicalActivityLevel"]))
print(pd.crosstab(data["Gender"], data["PhysicalActivityLevel"], normalize=True))
print(pd.crosstab(data["ObesityCategory"], data["PhysicalActivityLevel"]))
print(pd.crosstab(data["ObesityCategory"], data["PhysicalActivityLevel"], normalize=True))

#c (one three-way frequency table)
print(pd.crosstab([data["Gender"], data["ObesityCategory"]], data["PhysicalActivityLevel"]))
print(pd.crosstab([data["Gender"], data["ObesityCategory"]], data["PhysicalActivityLevel"], normalize=True))


import matplotlib.pyplot as plt

#6 Mutlivariate graphical EDA
#6.1.Visualizing statistical relationships (5 plots):

#a) Faceting feature (col parameter in the relplot() function
sns.relplot(data, y='Height', x= 'BMI', col='Gender')
plt.show()

#b)  5 variables at once (x, y, hue, size, col)
sns.relplot(data, x= 'Height', y= 'Weight', hue= 'BMI', size= 'Age' , col= 'Gender')
plt.show()

#c) plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)
sns.relplot(data, x='BMI', y= 'Weight', kind= 'line')
plt.show()

#d) illustrating standard deviation
sns.relplot(data, x='Age', y= 'Weight', kind= 'line', errorbar='sd')
plt.show()

#e) plot including linear regression
sns.lmplot(data, x='Age', y= 'BMI')
plt.show()

#6.2. Visualizing categorical data (10 plots):

#a) categorical scatter plot with jitter enabled
sns.catplot(data, y= 'Weight', x= 'PhysicalActivityLevel', jitter= True)
plt.show()

#b)  categorical scatter plot with jitter disabled (explain your choice of variable for this one)
sns.catplot(data, y= 'BMI', x= 'PhysicalActivityLevel', jitter= False)
plt.show()

#This choice of variable shows the min and max level of BMI level per physical activity level
#c) “beeswarm” plot representing 3 variables
sns.catplot(data, y= 'BMI', x= 'PhysicalActivityLevel', hue= 'Gender', kind= 'swarm')
plt.show()

#d) boxplot representing 3 variables
sns.catplot(data, y= 'BMI', x= 'PhysicalActivityLevel', hue= 'Gender', kind= "box")
plt.show()

#e)  box plot showing the shape of the distribution (boxenplot())
sns.boxenplot(data, x= 'PhysicalActivityLevel', y= "BMI")
plt.show()

#f) split violin plot representing 3 variables with bandwidth adjusted for better visualization
sns.violinplot(data, x= 'ObesityCategory', y= 'Age', hue= "Gender", bw_adjust= 0.6, split= True)
plt.show()

#g) violin plot with scatter points inside the violin shapes
sns.catplot(data, y= 'Age', x= 'ObesityCategory', kind= 'violin', inner= None)
sns.swarmplot(data, y= 'Age', x= 'ObesityCategory', color= 'k', size= 2.5)
plt.show()

#h) bar plot representing 3 variables showing 97% confidence intervals
sns.catplot(data, x= 'ObesityCategory', y= 'Age', hue= 'Gender', kind= 'bar', errorbar= ('pi', 97))
plt.show()

#i) point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
sns.pointplot(data, x= 'Weight', y= 'ObesityCategory', hue= 'Gender', linestyle= '--', errorbar= ('pi',90))
plt.show()

#j) bar plot showing the number of observations in each category
sns.countplot(data, x= 'ObesityCategory')
plt.show()

#6.3. Visualizing bivariate distributions (3 plots):

#a) 1 “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.
sns.displot(data, x= 'ObesityCategory', y= 'Height', binwidth= (2, 1.5) , cbar= True)
plt.show()

#b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).
sns.displot(data, x= 'Height', y= 'Age', kind= 'kde', bw_adjust= .8)
plt.show()

#c) 1 “heatmap” plot representing 3 variables, again of kind kde.
sns.displot(data, x= 'PhysicalActivityLevel', y= 'BMI', col= 'Gender', kind= 'kde')
plt.show()
