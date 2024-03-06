

from sympy import*
p=Point(4,-2)
print('\nReflection Through Y-axis = ')
p.transform(Matrix([[-1,0,0],[0,1,0],[0,0,1]]))
print('\nScaling in X-coordinate by factor 3 = ')
p.scale(3,0)
print('\nScaling in Y-coordinate by factor 2.5 =')
p.scale(0,2.5)
print('\nReflection Through Y=-X  = ')
p.transform(Matrix([[0,-1,0],[-1,0,0],[0,0,1]]))
     
