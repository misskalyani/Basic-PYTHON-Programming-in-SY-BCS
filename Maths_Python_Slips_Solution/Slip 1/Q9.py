
from sympy import *
p=Point(3,-1)
     

print("Reflection through y-axis :: ", p.transform(Matrix([[1,0,0],[0,-1,0],[0,0,1]])))
#p.reflect(Line(y))
     

print("scaling in x=2 :: ",p.scale(2,0))
     

print("scaling in y=1.5 :: ",p.scale(0,1.5))
     

#p.reflect(Line(x-y))  
print("reflection line x-y :: ",p.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]])))
