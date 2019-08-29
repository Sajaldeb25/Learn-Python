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