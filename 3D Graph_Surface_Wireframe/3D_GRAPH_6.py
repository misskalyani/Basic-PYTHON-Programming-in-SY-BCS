from mpl_toolkits import mplot3d
import numpy as np
from pylab import *
def f(x,y):
    return log(x**2+y**2)
x = np.linspace(-5,5,30)
y = np.linspace(-5,5,30)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
ax=axes(projection='3d')
ax.contour3D(X,Y,Z,50)
xlabel('x')
ylabel('y')
title('3D contour')
show()
