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
    
# Taylor series for cosine function
x = np.arange(-5*math.pi, 5*math.pi, 0.0001)

y1 = np.cos(x)

k = int(input('Enter the degree upto which taylor series will be taken = '))

y2=0
for i in range(k):
    y2 += ((-1)**i)*(x**(2*i)) / (fact(2*i))
    
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.ylabel('cos(x)')
plt.xlabel('x')
plt.legend(['cosine', 'taylor'])
plt.ylim(-3,3)
plt.show()

