from sympy import *
x,y = symbols('x y')
a = Point(0,0)
b = Point(5,0)
c = Point(3,3)
t = Triangle(a,b,c)
print("Area : ",t.area)
print("Perimeter :",t.perimeter)
