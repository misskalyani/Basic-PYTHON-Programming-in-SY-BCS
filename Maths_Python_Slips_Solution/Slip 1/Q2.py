
from mpl_toolkits import mplot3d
import numpy as np
from pylab import*
x = np.linspace(-5,5,10)
y = np.exp(-x**2)
ax = axes(projection = '3d')
ax.plot(x,y,'-.^g')
show()
