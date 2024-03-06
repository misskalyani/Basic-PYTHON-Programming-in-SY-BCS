
from mpl_toolkits import mplot3d
import numpy as np
from pylab import*
def f(x,y):
    return sin(x*2+y*2)
x = np.linspace(0,10,100)
y = np.linspace(0,10,100)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
ax=axes(Projection='3D')
ax.contour3D(x,y,z,50)
xlabel('x')
ylabe('y')
title('3D contour')
show()
