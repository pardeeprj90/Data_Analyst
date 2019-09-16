# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:47:54 2019

@author: Pradeep Kumar
"""
import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
#print(df.head())

#plt.plot(df.species,df.petal_length)

#plt.xlabel("length")
#plt.ylabel("width")
#plt.title("SeaBorn Data Analysis",fontsize=30)
#plt.style.use('fivethirtyeight')
#plt.plot(df.sepal_length,df.sepal_width,label="Length",color="tomato",linewidth=1,linestyle='--')
#plt.plot(df.petal_length,df.petal_width,label="Width",color="orange",linewidth=2,linestyle='--')
#plt.legend()
#plt.show()

print(plt.style.available)