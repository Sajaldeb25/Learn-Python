# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:03:28 2019

@author: Ryans
"""

# Learn python 


import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.random.randn(100)
plt.plot(x)
plt.show()

np.sqrt(9) 

from numpy import sqrt
sqrt(9) # do the same job




## printing the same graph using loop and list 
ts_length = 100
values = []   # Empty list

for i in range(ts_length):
    e = np.random.randn()
    values.append(e)

plt.plot(values)
plt.show()