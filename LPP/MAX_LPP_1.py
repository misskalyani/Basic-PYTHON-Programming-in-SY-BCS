from pulp import*
model = LpProblem(name ="Solution",sense=LpMaximize)
x=LpVariable(name="x",lowBound=0)
y=LpVariable(name="y",lowBound=0)
z=LpVariable(name="z",lowBound=0)
model +=(4*x+6*y<=24)
model +=(5*x+3*y<=15)
model +=150*x+75*y
print('\n',model)
print('\n',model.solve())
print('\n Model Objective Value = ',model.objective.value())
print('\n Value Of x = ',x.value())
print('\n Value Of y = ',y.value())
