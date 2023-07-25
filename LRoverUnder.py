# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:07:15 2023

@author: be

NFLdata

"""
import regression as lr
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# read in the data
# look at column names, and I want to plot betttin line versus what actually 
# happened

NFLdata = pd.read_csv('NFL2022')
type(NFLdata)
names = list(NFLdata)
print(names)

# set up y which is the delta score = function of x, x=betting line
# delta = home team score - visit team score

x = NFLdata['overUnder']
y = NFLdata['hScore'] + NFLdata['vScore']

b0, b1 = lr.estimate_coef(x, y)
print(b0, b1)

histAx = np.linspace(10,90)
plt.hist(x, alpha = 0.35, label='line', bins=20)
plt.hist(y, alpha = 0.45, label = 'actual spread', bins=20)
plt.xlabel('points')
plt.ylabel('frequency')
plt.legend()
plt.grid()
plt.show()

plt.plot(x, y, 'o')
xAxis = np.linspace(-20, 15)

yPred = b0+b1*xAxis
plt.plot(xAxis, yPred, color='red')
plt.xlabel('line')
plt.ylabel('home score-visit score')
plt.hlines(y=0, xmin=30, xmax=60, color='orange')
plt.grid()

