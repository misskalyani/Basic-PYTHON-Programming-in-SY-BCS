from pylab import*
import numpy as np
x=np.linspace(-2*pi,2*pi,100)
y=cos(x)
z=sin(x)
plot(x,y)
plot(x,z)
show()
