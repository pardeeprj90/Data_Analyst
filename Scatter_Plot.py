# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:53:00 2019

@author: Pradeep Kumar
"""

import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/pardeeprj90/CSV_File_For_Data_Analysis/master/mtcars.csv")
print(df.head())
plt.xlabel('Miles per gallon')
plt.ylabel('Weight of car')
#plt.title("Sepal length & Width representation in Scatter Plot",fontsize=10)
plt.scatter(df.mpg,df.wt,color='red',marker='s')
plt.show()