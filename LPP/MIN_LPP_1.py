from pulp import*
model = LpProblem(name ="Solution",sense=LpMinimize)
x=LpVariable(name="x",lowBound=0)
y=LpVariable(name="y",lowBound=0)
z=LpVariable(name="z",lowBound=0)
model +=(x+y<=5)
model +=(x<=4)
model +=(y<=2)
model +=3.5*x+2*y
print('\n',model)
print('\n',model.solve())
print('\n Model Objective Value = ',model.objective.value())
print('\n Value Of x = ',x.value())
print('\n Value Of y = ',y.value())

