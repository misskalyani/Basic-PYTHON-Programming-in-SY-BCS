from sympy import*
x,y=symbols('x y')
a=Point(0,0)
b=Point(6,0)
c=Point(4,4)
t=Triangle(a,b,c)
print('\nArea = ',t.area)
print('\nPerimeter = ',t.perimeter)
