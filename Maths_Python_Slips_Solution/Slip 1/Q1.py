from sympy import *
a = Point(5,-2)
b = Point(4,3)
s=Segment(a,b)
s=s.rotate(pi)
s=s.scale(2,0)
points=s.points
points
p=points[0]
q=points[1]
p1=p.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]]))
q1=q.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]]))
p1=p.transform(Matrix([[1,0,0],[4,1,0],[0,0,1]]))
q1=q.transform(Matrix([[1,0,0],[4,1,0],[0,0,1]]))
Segment(p1,q1)
