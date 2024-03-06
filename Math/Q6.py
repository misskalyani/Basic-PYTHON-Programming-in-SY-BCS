from sympy import *
s = Segment(Point(5,3),Point(1,4))
x,y = symbols('x y')
l = Line(x-y+1)
s.reflect(l)
