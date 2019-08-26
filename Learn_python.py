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
loop_length = 100
values = []   # Empty list

for i in range(loop_length):
    e = np.random.randn()
    values.append(e)

plt.plot(values)
plt.show()



##explain list
x = ['Sajal',22, 'cse']
x.append(50000)
x.pop()
x.append(60000)


## printing the same graph using while loop
n = 100
value = []
i = 0
while i<n:
    e = np.random.randn()
    value.append(e)
    i = i+1

plt.plot(value)
plt.show()


## printing the same graph using while loop
def generate_data(n):
    value = []
    i = 0
    while i<n:
        e = np.random.randn()
        value.append(e)
        i = i+1
        
data = generate_data(100)
plt.plot(value)
plt.show()


## printing the same graph using conndition
def generate_data(n,g_type):
    value = []
    i = 0
    while i<n :
        if g_type == 'A':
            e = np.random.uniform(4, 5)
        else:
            e = np.random.randn()
        value.append(e)
        i = i+1
    return value

data = generate_data(100, 'A')
plt.plot(data)
plt.show()


## same graph 
def generate_data(n, generator_type):
    e_values = []
    for i in range(n):
        e = generator_type()
        e_values.append(e)
    return e_values

data = generate_data(100, np.random.uniform)
plt.plot(data)
plt.show()


## List 
animals = ['dog', 'cat', 'bird']
plurals = [animal + 's' for animal in animals]
plurals


doubles = [2 * x for x in range(11)]
doubles
##--------------List End--------------------

##Excersise 1 (Factorial )
 
def factorial(n):
    k = 1
    for i in range(n):
        k = k*(i+1)
    return k

factorial(5)







