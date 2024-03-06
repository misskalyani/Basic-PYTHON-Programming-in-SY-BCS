import matplotlib.pyplot as plt
import numpy as np
items = ['clothing','food','rent','petrol','misc']
exp = [600,4000,2000,1500,700]
plt.bar(items,exp,width = 0.8,color = 'green')
plt.xlabel('items')
plt.ylabel('exp')
plt.show()
