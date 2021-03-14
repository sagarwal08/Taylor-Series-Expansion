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
    
#Taylor Series for Log function

x = np.arange(-0.5, 5, 0.00001)

y1 = np.log(x)

k = int(input('Enter the degree upto which taylor series will be taken = '))

y2=0
for i in range(1,k+1):
    y2 +=  ((-1)**(i-1))*((x-1)**(i) / (fact(i)))
    
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.ylabel('log(x)')
plt.xlabel('x')
plt.legend(['log', 'taylor'])
plt.ylim(-3,4)
plt.show()

