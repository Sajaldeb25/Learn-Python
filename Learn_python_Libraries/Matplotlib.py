# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:59:53 2019

@author: Ryans
"""

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

## tan cruve
x = np.linspace(0, 10, 200)
y = np.tan(x)

plt.plot(x, y, 'c-', linewidth=1)
plt.show()

## cos cruve
x = np.linspace(0, 20, 5) # 0 to 20 with 5 itiration
y = np.cos(x)

plt.plot(x, y, 'c-', linewidth=1)
plt.show()


## sin cruve
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'c-', linewidth=1)
plt.show()


fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.9)
ax.legend()
plt.show()


fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.9)
ax.legend(loc='upper center')
plt.show()


fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label='$y=\sin(x)$', alpha=0.6)
ax.legend(loc='upper center')
ax.set_yticks([-1,-.5, 0, .5, 1])
plt.title('Test plot')
plt.show()



##More plot on one axis

from scipy.stats import norm
from random import uniform

fig, ax = plt.subplots()
x = np.linspace(-4, 4, 150)
for i in range(3):
    print(i)
    m, s = uniform(-1, 1), uniform(1, 2)
    y = norm.pdf(x, loc=m, scale=s)
    current_label = '$\mu = {m:.2}$'
    ax.plot(x, y, linewidth=2, alpha=0.6, label=current_label)
ax.legend()
plt.show()