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

##Exercise 2 (Binomial function)
from numpy.random import uniform
def binomial(n, p):
    count = 0
    for i in range(n):
        v = uniform()
        if v<p:
            count = count + 1
    return count

binomial(10, 0.4)


##Exercise 4 ( )
from numpy.random import uniform

pay = 0
cnt = 0

for i in range (10):
    x = uniform()
    if x < 0.5:
        cnt = cnt+1
    else:
        cnt = 0
    
    if cnt == 3:
        pay = pay +1

print(pay)


## Exexcise 5 
a = 0.9
length = 200
current_x = 0

x_values = []
for i in range(length+1):
    x_values.append(current_x)
    current_x = a*current_x + np.random.randn()

plt.plot(x_values)
plt.show()

    
## legand
import numpy as np
import matplotlib.pyplot as plt

x = [np.random.randn() for i in range(100)]
plt.plot(x, label="white noise")
plt.legend()
plt.show()



## legand with 3 values
a_s = [0.0, 0.8, 0.98]
length = 200

for a in a_s:
    x_values = []
    current_x = 0
    for i in range(length):
        x_values.append(current_x)
        current_x = a*current_x + np.random.randn()
    plt.plot(x_values, label= 'a = {a}')
plt.legand()
plt.show()
