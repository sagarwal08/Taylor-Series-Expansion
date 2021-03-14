#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import math

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
#Taylor Series for Exponential Function

x = np.arange(-3, 5, 0.00001)

y1 = np.exp(x)

k = int(input('Enter the degree upto which taylor series will be taken = '))

y2=0
for i in range(k):
    y2 += (x**i) / (fact(i))
    
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.ylabel('exp(x)')
plt.xlabel('x')
plt.legend(['exp', 'taylor'])
plt.show()

