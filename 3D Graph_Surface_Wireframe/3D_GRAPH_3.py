from mpl_toolkits import mplot3d
import numpy as np
from pylab import *
def f(x,y):
    return (sin(x)+cos(y))
x = np.linspace(-2*pi,2*pi,30)
y = np.linspace(-2*pi,2*pi,30)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
ax=axes(projection='3d')
ax.contour3D(X,Y,Z,50)
xlabel('x')
ylabel('y')
title('3D contour')
show()
