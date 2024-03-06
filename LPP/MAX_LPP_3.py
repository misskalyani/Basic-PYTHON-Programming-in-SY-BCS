from pulp import*
model = LpProblem(name ="Solution",sense=LpMaximize)
x=LpVariable(name="x",lowBound=0)
y=LpVariable(name="y",lowBound=0)
z=LpVariable(name="z",lowBound=0)
model +=(x-y<=1)
model +=(x+y<=2)
model +=x+y
print('\n',model)
print('\n',model.solve())
print('\n Model Objective Value = ',model.objective.value())
print('\n Value Of x = ',x.value())
print('\n Value Of y = ',y.value())
print('\n Value Of z = ',z.value())
