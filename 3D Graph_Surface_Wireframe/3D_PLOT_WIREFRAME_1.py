from mpl_toolkits import mplot3d
import numpy as np
from pylab import *
def f(x,y):
    return sin(x)+cos(y)
x = np.linspace(-5,5,30)
y = np.linspace(-5,5,30)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
ax=axes(projection='3d')
ax.plot_wireframe(X,Y,Z,50)
xlabel('x')
ylabel('y')
title('Wireframe')
show()
