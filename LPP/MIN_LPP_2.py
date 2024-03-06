from pulp import*
model = LpProblem(name ="Solution",sense=LpMinimize)
x=LpVariable(name="x",lowBound=0)
y=LpVariable(name="y",lowBound=0)
z=LpVariable(name="z",lowBound=0)
model +=(x+1.5*y+1.5*z<=1)
model +=(3*x+2*y+z<=8)
model +=x+2*y+z
print('\n',model)
print('\n',model.solve())
print('\n Model Objective Value = ',model.objective.value())
print('\n Value Of x = ',x.value())
print('\n Value Of y = ',y.value())
print('\n Value Of z = ',z.value())
